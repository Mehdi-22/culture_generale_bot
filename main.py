import time
import logging
from datetime import datetime
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
from config import DIGEST_HOUR, WEEKLY_SCHEDULE, POLE_KEYWORDS
from storage import Storage
from scraper import WebScraper
from generator import CompositionGenerator
from telegram_bot import TelegramSender

storage = Storage()
scraper = WebScraper(storage)
generator = CompositionGenerator()
sender = TelegramSender()


def run_digest():
    weekday = datetime.now().weekday()
    schedule = WEEKLY_SCHEDULE[weekday]
    pole = schedule["pole"]
    source_names = schedule["sources"]
    keywords = POLE_KEYWORDS.get(pole, [])

    logging.info(f"=== Digest du jour — {pole} ===")
    articles = scraper.get_articles_for_pole(source_names, keywords)

    if not articles:
        logging.info("Aucun article pertinent trouve pour ce pole aujourd'hui")
        sender.send(f"Aucun nouvel article pour le digest {pole} aujourd'hui.")
        return

    storage.save_pending(articles)
    ok = sender.send_digest(pole, articles)
    if ok:
        logging.info(f"Digest envoye : {len(articles)} articles")
    else:
        logging.error("Echec envoi digest Telegram")


def check_user_commands():
    offset = storage.load_update_offset()
    updates = sender.get_updates(offset)

    if not updates:
        return

    from config import TELEGRAM_CHAT_ID
    pending = storage.load_pending()
    new_offset = offset

    for update in updates:
        update_id = update.get("update_id", 0)
        new_offset = max(new_offset, update_id + 1)

        message = update.get("message", {})
        chat_id = str(message.get("chat", {}).get("id", ""))
        text = message.get("text", "").strip()

        if chat_id != str(TELEGRAM_CHAT_ID):
            continue
        if not text:
            continue

        numbers = sender.parse_selection(text)
        if not numbers:
            continue

        logging.info(f"Selection recue: {numbers}")
        for num in numbers:
            article = pending.get(str(num))
            if not article:
                sender.send(f"Article {num} introuvable. Demande un nouveau digest.")
                continue

            logging.info(f"Generation composition: {article['title'][:60]}")
            composition = generator.generate(article)
            if not composition:
                logging.warning(f"Generation echouee pour article {num}")
                sender.send(f"Erreur generation composition pour l'article {num}.")
                continue

            message_text = sender.format_message(article, composition)
            ok = sender.send(message_text)

            topic_hash = storage.hash(article["title"])
            storage.mark_seen(topic_hash, article["title"], article["url"])

            if ok:
                logging.info(f"Composition article {num} envoyee et marquee")
            else:
                logging.error(f"Echec envoi composition article {num}")

            time.sleep(15)

    storage.save_update_offset(new_offset)


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_digest, "cron", hour=DIGEST_HOUR, minute=0)
    scheduler.add_job(check_user_commands, "interval", seconds=60)
    scheduler.start()

    logging.info(f"Bot demarre — digest chaque jour a {DIGEST_HOUR}h00, polling commandes toutes les 60s")

    run_digest()

    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        logging.info("Arret du bot")
        scheduler.shutdown()
        scraper.close()
