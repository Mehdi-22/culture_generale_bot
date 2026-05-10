# Bot Culture Générale — Telegram (Gemini)

## Contexte
Bot de surveillance web qui détecte des sujets d'actualité et génère automatiquement
une composition complète selon la méthode de composition militaire marocaine,
puis l'envoie via Telegram. Utilise Google Gemini API (gratuit).

## Stack Technique
- Python 3.10+
- Google Gemini API (gemini-2.0-flash) — GRATUIT
- python-telegram-bot pour Telegram
- feedparser + BeautifulSoup pour le scraping
- APScheduler pour la planification

## Structure du Projet
```
bot_culture_generale/
├── main.py
├── config.py
├── scraper.py
├── generator.py
├── telegram_bot.py
├── storage.py
├── prompts/
│   ├── __init__.py
│   └── methode.py
├── data/
│   └── seen_topics.json
├── .env
├── .env.example
├── requirements.txt
├── bot.log
└── README.md
```

## Variables d'Environnement (.env)
```
GEMINI_API_KEY=AIzaSy-votre-cle-ici
TELEGRAM_BOT_TOKEN=123456789:ABC...
TELEGRAM_CHAT_ID=votre-chat-id
CHECK_INTERVAL_HOURS=6
```

## Méthode de Composition — Structure 21 Paragraphes

### INTRODUCTION (4 §)
- §1  PRÉAMBULE : contexte général, jamais d'éléments de réponse
- §2  QUESTION POSÉE : "il serait judicieux de s'interroger sur..."
- §3  IDÉE MAÎTRESSE : 1 seule phrase, répond directement à la question
- §4  ANNONCE DU PLAN : "Pour s'en convaincre, seront examinés..."

### DÉVELOPPEMENT PARTIE 1 (5 §)
- §5  ID1 : idée directrice juxtaposant les 3 IS
- §6  IS11 : "De prime abord," + idée + fait + exemple
- §7  IS12 : "Par ailleurs," + idée + fait + exemple
- §8  IS13 : "De surcroît," + idée + fait + exemple
- §9  Conclusion P1 + transition : "Partant,"

### DÉVELOPPEMENT PARTIE 2 (5 §)
- §10 ID2 : "Outre les..."
- §11 IS21 : "Assurément,"
- §12 IS22 : "De même,"
- §13 IS23 : "De surcroît,"
- §14 Conclusion P2 + transition : "Dès lors,"

### DÉVELOPPEMENT PARTIE 3 (5 §)
- §15 ID3 : "Outre... et..."
- §16 IS31 : "Effectivement,"
- §17 IS32 : "Aussi,"
- §18 IS33 : "Enfin,"
- §19 Conclusion P3 SANS transition : "Ainsi,"

### CONCLUSION (2 §)
- §20 Reformulation IM : "En définitive,"
- §21 Ouverture : jamais une question

## Gabarits d'Idée Maîtresse
- "Bien que [X], il n'en demeure pas moins que [Y et Z]"
- "Les défaillances liées à [X] n'occultent point les avantages en matière de [Y]"
- "Ayant des objectifs visant [X], [sujet] constituerait un levier dans la mesure où [Y]"
- "Au-delà de [X] et [Y], les défis sont liés surtout à [Z]"

## Règles Absolues
- Phrases courtes (15-25 mots)
- Vocabulaire simple
- IS = Idée abstraite + Fait + Exemple
- Vérifier Limites : Temps / Espace / Domaine
- IM = 1 seule phrase sans point ni point-virgule

## Modèle Gemini
- Modèle : gemini-2.0-flash
- temperature : 0.7
- max_output_tokens : 4000
- system_instruction : SYSTEM_PROMPT complet dans prompts/methode.py

## Pipeline d'Exécution
1. Scraping RSS/HTML des sites configurés (toutes les 6h)
2. Filtrage par mots-clés pertinents
3. Vérification des doublons (seen_topics.json)
4. Génération Gemini (composition 21 §)
5. Envoi Telegram en chunks de 4000 chars
6. Marquage du sujet comme traité

## Thématiques des Sujets
Économie, sécurité, défense, environnement, géopolitique, technologie militaire,
gouvernance, diplomatie, relations internationales, Maroc/Maghreb/Afrique
