import time
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

from apscheduler.schedulers.background import BackgroundScheduler
from config import CHECK_INTERVAL_HOURS
from storage import Storage
from scraper import WebScraper
from generator import CompositionGenerator
from telegram_bot import TelegramSender

storage = Storage()
scraper = WebScraper(storage)
generator = CompositionGenerator()
sender = TelegramSender()


def run_pipeline():
    logging.info("=== Debut du cycle de surveillance ===")
    storage.cleanup_old_entries()
    articles = scraper.get_new_articles()
    logging.info(f"Articles a traiter: {len(articles)}")

    for article in articles:
        logging.info(f"Traitement: {article['title'][:80]}")
        composition = generator.generate(article)
        if not composition:
            logging.warning("Generation echouee, article ignore")
            continue

        message = sender.format_message(article, composition)
        ok = sender.send(message)

        topic_hash = storage.hash(article["title"])
        storage.mark_seen(topic_hash, article["title"], article["url"])

        if ok:
            logging.info("Article envoye et marque")
        else:
            logging.error("Echec envoi Telegram")

        time.sleep(30)

    logging.info("=== Fin du cycle ===")


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_pipeline, "interval", hours=CHECK_INTERVAL_HOURS)
    scheduler.start()
    logging.info(f"Bot demarre — cycle toutes les {CHECK_INTERVAL_HOURS}h")

    run_pipeline()

    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        logging.info("Arret du bot")
        scheduler.shutdown()
        scraper.close()
