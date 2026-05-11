import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
CHECK_INTERVAL_HOURS = int(os.getenv("CHECK_INTERVAL_HOURS", "24"))
CLAUDE_MODEL = "claude-sonnet-4-6"

DIGEST_HOUR = int(os.getenv("DIGEST_HOUR", "9"))

WEEKLY_SCHEDULE = {
    0: {"pole": "Maroc / Maghreb",          "sources": ["MAP News", "Hespress", "IRES", "Geopolitique.ma", "IRIS"]},
    2: {"pole": "Economie & Developpement", "sources": ["Jeune Afrique", "UNECA", "Le Monde"]},
    4: {"pole": "Geopolitique / RI",        "sources": ["RFI", "Le Monde", "Ifri", "IRIS"]},
}

BOOST_KEYWORDS = [
    "drone", "drones", "IA", "intelligence artificielle", "AI", "robotique",
    "cybersecurite", "cybersécurité", "technologie militaire", "satellite",
    "guerre electronique", "guerre électronique", "renseignement militaire",
    "Maroc Afrique", "partenariat militaire", "cooperation defense",
    "coopération défense", "Forces Armees Royales", "FAR", "marine royale",
    "OTAN Afrique", "base militaire", "accord defense", "accord défense",
    "industrie armement", "industrie d'armement", "guerre hybride",
    "proliferation", "prolifération", "conflit arme", "conflit armé",
]

POLE_KEYWORDS = {
    "Maroc / Maghreb": [
        "Maroc", "Maghreb", "Algerie", "Algérie", "Tunisie", "Libye", "Sahel",
        "Rabat", "Alger", "Tunis", "Tripoli", "marocain", "maghrebin",
    ],
    "Afrique — Securite": [
        "Afrique", "securite", "sécurité", "gouvernance", "criminalite", "terrorisme",
        "conflit", "paix", "Mali", "Niger", "Burkina", "Sahel", "jihadiste",
        "security", "governance", "conflict", "peace", "Africa",
    ],
    "Economie & Developpement": [
        "economie", "économie", "croissance", "dette", "commerce", "developpement",
        "développement", "investissement", "PIB", "financement", "budget", "reforme",
        "economy", "growth", "trade", "development", "investment",
    ],
    "Defense & Strategie": [
        "defense", "défense", "militaire", "armement", "strategie", "stratégie",
        "OTAN", "nucleaire", "nucléaire", "renseignement", "armée", "marine",
        "military", "defense", "strategy", "weapons", "nuclear",
    ],
    "Geopolitique / RI": [
        "geopolitique", "géopolitique", "diplomatie", "international", "ONU", "relations",
        "souverainete", "accord", "sommet", "traite", "traité", "negociation",
        "geopolitics", "diplomacy", "international", "UN", "summit", "treaty",
    ],
    "Afrique panafricaine": [
        "Afrique", "panafricain", "Union africaine", "Sahel", "developpement",
        "integration", "Africa", "African Union", "continental",
    ],
}

SITES_TO_MONITOR = [
    # priority: 1=think tanks/institutionnels, 2=medias reference, 3=medias locaux
    {"url": "https://www.lemonde.fr/rss/une.xml", "name": "Le Monde", "type": "rss", "priority": 2},
    {"url": "https://www.rfi.fr/fr/rss", "name": "RFI", "type": "rss", "priority": 2},
    {"url": "https://www.mapnews.ma/fr/rss.xml", "name": "MAP News", "type": "rss", "priority": 3},
    {"url": "https://www.hespress.com/feed", "name": "Hespress", "type": "rss", "priority": 3},
    {"url": "https://www.iris-france.org/feed/", "name": "IRIS", "type": "rss", "priority": 1},
    {"url": "http://www.uneca.org/rss.xml", "name": "UNECA", "type": "rss", "priority": 1},
    {"url": "https://www.jeuneafrique.com/feed/", "name": "Jeune Afrique", "type": "rss", "priority": 2},
    {"url": "https://feeds.bbci.co.uk/afrique/rss.xml", "name": "BBC Afrique", "type": "rss", "priority": 2},
    {
        "url": "https://www.ifri.org/fr/publications",
        "name": "Ifri",
        "type": "html",
        "selector": ".views-row a",
        "base_url": "https://www.ifri.org",
        "min_title_len": 30,
        "priority": 1,
    },
    {
        "url": "https://geopolitique.ma",
        "name": "Geopolitique.ma",
        "type": "html",
        "selector": "article a[href]",
        "base_url": "https://geopolitique.ma",
        "min_title_len": 20,
        "priority": 3,
    },
    {
        "url": "https://www.ires.ma/fr/publications",
        "name": "IRES",
        "type": "playwright",
        "selector": "a:has(h2)",
        "base_url": "https://www.ires.ma",
        "min_title_len": 25,
        "wait_ms": 1500,
        "priority": 1,
    },
    {
        "url": "https://issafrica.org/iss-today",
        "name": "ISS Africa",
        "type": "playwright",
        "selector": "a[href*='/iss-today/']",
        "base_url": "https://issafrica.org",
        "min_title_len": 20,
        "text_clean": "after_newline",
        "wait_ms": 4000,
        "priority": 1,
    },
]

RELEVANT_KEYWORDS = [
    # Francais
    "économie", "economie", "sécurité", "securite", "défense", "defense",
    "environnement", "géopolitique", "geopolitique", "technologie", "gouvernance",
    "développement", "developpement", "diplomatie", "militaire", "stratégie", "strategie",
    "crise", "réforme", "reforme", "international", "terrorisme", "énergie", "energie",
    "agriculture", "commerce", "industrie", "conflit", "nucléaire", "nucleaire",
    "cybersécurité", "cybersecurite", "ONU", "OTAN", "Maroc", "Maghreb", "Afrique",
    "Europe", "Moyen-Orient", "guerre", "paix", "accord", "sommet", "traité", "traite",
    "Sahel", "Algérie", "Algerie", "Tunisie", "Libye", "Mali", "Niger",
    # Anglais (pour ISS Africa et BBC Afrique)
    "security", "defense", "governance", "conflict", "peace", "Africa", "Sahel",
    "economy", "geopolitics", "diplomacy", "military", "terrorism", "climate",
    "development", "reform", "crisis", "Morocco", "Maghreb", "regional",
]
