# Bot Culture Générale — Telegram (Gemini)

Bot Python qui surveille des sites d'actualité, génère automatiquement une composition
selon la méthode militaire marocaine en 21 paragraphes, et l'envoie via Telegram.

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Copiez `.env.example` en `.env` et renseignez vos clés :

```bash
cp .env.example .env
```

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Clé API Google Gemini (gratuit sur aistudio.google.com) |
| `TELEGRAM_BOT_TOKEN` | Token du bot Telegram (via @BotFather) |
| `TELEGRAM_CHAT_ID` | ID du chat ou canal Telegram cible |
| `CHECK_INTERVAL_HOURS` | Intervalle de vérification en heures (défaut : 6) |

## Lancement

```bash
python main.py
```

Le bot démarre immédiatement un premier cycle, puis tourne en boucle toutes les `CHECK_INTERVAL_HOURS` heures.
Les logs apparaissent dans la console et dans `bot.log`.

## Ajouter des sites

Dans `config.py`, ajoutez un dict dans `SITES_TO_MONITOR` :

```python
{"url": "https://example.com/feed.xml", "name": "Mon Site", "type": "rss"}
# ou
{"url": "https://example.com/actualites", "name": "Mon Site", "type": "html"}
```

## Structure

```
├── main.py           # Point d'entrée + scheduler
├── config.py         # Variables de configuration
├── scraper.py        # Scraping RSS / HTML
├── generator.py      # Génération Gemini
├── telegram_bot.py   # Envoi Telegram
├── storage.py        # Déduplication seen_topics.json
├── prompts/
│   └── methode.py    # Prompts système et utilisateur
├── data/
│   └── seen_topics.json
├── .env
└── requirements.txt
```
