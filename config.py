import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
CHECK_INTERVAL_HOURS = int(os.getenv("CHECK_INTERVAL_HOURS", "24"))
CLAUDE_MODEL = "claude-sonnet-4-6"

SITES_TO_MONITOR = [
    # --- Medias generalistes (base existante) ---
    {"url": "https://www.lemonde.fr/rss/une.xml", "name": "Le Monde", "type": "rss"},
    {"url": "https://www.rfi.fr/fr/rss", "name": "RFI", "type": "rss"},
    {"url": "https://www.mapnews.ma/fr/rss.xml", "name": "MAP News", "type": "rss"},
    {"url": "https://www.hespress.com/feed", "name": "Hespress", "type": "rss"},

    # --- Pole Maghreb / Geopolitique ---
    # IRIS Observatoire du Maghreb : think tank FR, analyses geopolitiques Maghreb/crises
    {"url": "https://www.iris-france.org/feed/", "name": "IRIS", "type": "rss"},

    # --- Pole Afrique / Economie ---
    # UNECA : source ONU, economie africaine, gouvernance, integration regionale
    {"url": "http://www.uneca.org/rss.xml", "name": "UNECA", "type": "rss"},
    # Jeune Afrique : media de reference panafricain, politique + economie + securite
    {"url": "https://www.jeuneafrique.com/feed/", "name": "Jeune Afrique", "type": "rss"},
    # BBC Afrique : couverture continentale large, evenements et crises en temps reel
    {"url": "https://feeds.bbci.co.uk/afrique/rss.xml", "name": "BBC Afrique", "type": "rss"},

    # --- Pole HTML scraping (Phase 2) ---
    # Ifri : reference FR geopolitique, defense, energie, Maghreb
    {
        "url": "https://www.ifri.org/fr/publications",
        "name": "Ifri",
        "type": "html",
        "selector": ".views-row a",
        "base_url": "https://www.ifri.org",
        "min_title_len": 30,
    },
    # Geopolitique.ma : analyse locale marocaine, geostrategie regionale
    {
        "url": "https://geopolitique.ma",
        "name": "Geopolitique.ma",
        "type": "html",
        "selector": "article a[href]",
        "base_url": "https://geopolitique.ma",
        "min_title_len": 20,
    },
    # Note: IRES, Policy Center, ISS Africa sont JS-rendered (Selenium requis — Phase 3)
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
