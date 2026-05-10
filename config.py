import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
CHECK_INTERVAL_HOURS = int(os.getenv("CHECK_INTERVAL_HOURS", "24"))
CLAUDE_MODEL = "claude-sonnet-4-6"

SITES_TO_MONITOR = [
    {"url": "https://www.lemonde.fr/rss/une.xml", "name": "Le Monde", "type": "rss"},
    {"url": "https://www.rfi.fr/fr/rss", "name": "RFI", "type": "rss"},
    {"url": "https://www.mapnews.ma/fr/rss.xml", "name": "MAP News", "type": "rss"},
    {"url": "https://www.hespress.com/feed", "name": "Hespress", "type": "rss"},
]

RELEVANT_KEYWORDS = [
    "économie", "economie", "sécurité", "securite", "défense", "defense",
    "environnement", "géopolitique", "geopolitique", "technologie", "gouvernance",
    "développement", "developpement", "diplomatie", "militaire", "stratégie", "strategie",
    "crise", "réforme", "reforme", "international", "terrorisme", "énergie", "energie",
    "agriculture", "commerce", "industrie", "conflit", "nucléaire", "nucleaire",
    "cybersécurité", "cybersecurite", "ONU", "OTAN", "Maroc", "Maghreb", "Afrique",
    "Europe", "Moyen-Orient", "guerre", "paix", "accord", "sommet", "traité", "traite",
]
