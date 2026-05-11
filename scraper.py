import logging
import feedparser
import requests
from bs4 import BeautifulSoup
from storage import Storage
from config import SITES_TO_MONITOR, RELEVANT_KEYWORDS

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}
TIMEOUT = 10


class WebScraper:
    def __init__(self, storage: Storage):
        self.storage = storage

    def scrape_site(self, site_config: dict) -> list[dict]:
        articles = []
        try:
            if site_config["type"] == "rss":
                articles = self._scrape_rss(site_config)
            else:
                articles = self._scrape_html(site_config)
        except Exception as e:
            logging.error(f"Erreur scraping {site_config['name']}: {e}")
        return articles

    def _scrape_rss(self, site_config: dict) -> list[dict]:
        feed = feedparser.parse(site_config["url"])
        articles = []
        for entry in feed.entries[:20]:
            articles.append({
                "title": entry.get("title", ""),
                "summary": entry.get("summary", entry.get("description", "")),
                "url": entry.get("link", ""),
                "source": site_config["name"],
                "date": entry.get("published", ""),
            })
        return articles

    def _scrape_html(self, site_config: dict) -> list[dict]:
        resp = requests.get(site_config["url"], headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        articles = []
        base_url = site_config.get("base_url", "")
        selector = site_config.get("selector")
        min_title_len = site_config.get("min_title_len", 15)

        if selector:
            for a in soup.select(selector)[:20]:
                title = a.get_text(strip=True)
                if len(title) < min_title_len:
                    continue
                href = a.get("href", "")
                if href and not href.startswith("http") and base_url:
                    href = base_url.rstrip("/") + "/" + href.lstrip("/")
                articles.append({
                    "title": title,
                    "summary": "",
                    "url": href,
                    "source": site_config["name"],
                    "date": "",
                })
        else:
            for tag in soup.find_all(["h2", "h3"], limit=20):
                a = tag.find("a")
                if a:
                    title = a.get_text(strip=True)
                    href = a.get("href", "")
                    if href and not href.startswith("http") and base_url:
                        href = base_url.rstrip("/") + "/" + href.lstrip("/")
                    articles.append({
                        "title": title,
                        "summary": "",
                        "url": href,
                        "source": site_config["name"],
                        "date": "",
                    })
        return articles

    def is_relevant(self, article: dict) -> bool:
        text = (article.get("title", "") + " " + article.get("summary", "")).lower()
        return any(kw.lower() in text for kw in RELEVANT_KEYWORDS)

    def get_new_articles(self) -> list[dict]:
        new_articles = []
        for site in SITES_TO_MONITOR:
            articles = self.scrape_site(site)
            for article in articles:
                if not article["title"]:
                    continue
                topic_hash = Storage.hash(article["title"])
                if self.storage.is_seen(topic_hash):
                    continue
                if not self.is_relevant(article):
                    continue
                new_articles.append(article)
        logging.info(f"Nouveaux articles pertinents trouves: {len(new_articles)}")
        return new_articles
