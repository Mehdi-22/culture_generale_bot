# Bot Culture Générale CEM-CG — Telegram (Claude)

> Etat : v2.1 — RUNNING depuis 2026-05-11
> Stack : Claude Anthropic API (claude-sonnet-4-6) · Python 3.10+ · APScheduler · Playwright

---

## Contexte
Bot de veille géopolitique et militaire. Chaque lundi/mercredi/vendredi à 9h, il envoie
un digest thématique de 10 articles max sur Telegram. L'utilisateur choisit 1-2 numéros
et le bot génère une composition complète selon la méthode militaire marocaine (21 §).

---

## Stack Technique
- Python 3.10+
- **Claude Anthropic API** (claude-sonnet-4-6) — génération compositions
- APScheduler (BackgroundScheduler) — crons
- feedparser — scraping RSS
- requests + BeautifulSoup — scraping HTML
- Playwright (chromium headless) — sites JS-rendus (IRES, ISS Africa)
- Telegram Bot API (polling getUpdates) — envoi + réception commandes

---

## Structure du Projet
```
CEM-CG/
├── main.py              ← scheduler + run_digest() + check_user_commands() + send_weekly_planning()
├── config.py            ← WEEKLY_SCHEDULE, POLE_KEYWORDS, BOOST_KEYWORDS, SITES_TO_MONITOR
├── scraper.py           ← RSS / HTML / Playwright + get_articles_for_pole()
├── generator.py         ← appel Claude API, composition 21 §
├── telegram_bot.py      ← send_digest(), send(), get_updates(), parse_selection()
├── storage.py           ← seen_topics.json + pending_articles.json + update_offset.json
├── prompts/
│   ├── __init__.py
│   └── methode.py       ← SYSTEM_PROMPT complet méthode de composition
├── data/
│   ├── seen_topics.json       ← articles déjà composés (dédup)
│   ├── pending_articles.json  ← digest en attente de sélection utilisateur
│   └── update_offset.json     ← offset Telegram getUpdates
├── .env                 ← clés API (non commité)
├── .env.example
├── requirements.txt
└── bot.log
```

---

## Variables d'Environnement (.env)
```
ANTHROPIC_API_KEY=sk-ant-...
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=741215023
CHECK_INTERVAL_HOURS=24
DIGEST_HOUR=9
```

---

## Planning hebdomadaire (v2.1)

| Jour | Pôle | Sources principales |
|------|------|---------------------|
| **Lundi 9h** | Maroc / Maghreb | IRES, MAP News, Geopolitique.ma, IRIS, Hespress |
| **Mercredi 9h** | Économie & Développement | Jeune Afrique, UNECA, Le Monde |
| **Vendredi 9h** | Géopolitique / RI | RFI, Le Monde, Ifri, IRIS |
| **Dimanche 20h** | Planning semaine | Message automatique planning L/M/V |

---

## Sources configurées (12 sources)

| Source | Type | Priorité |
|--------|------|----------|
| IRIS | RSS | 1 — think tank |
| UNECA | RSS | 1 — institutionnel ONU |
| IRES | Playwright | 1 — institutionnel Maroc |
| ISS Africa | Playwright | 1 — sécurité africaine (EN) |
| Ifri | HTML | 1 — think tank FR |
| Le Monde | RSS | 2 — media référence |
| RFI | RSS | 2 — media référence |
| Jeune Afrique | RSS | 2 — media panafricain |
| BBC Afrique | RSS | 2 — media continental |
| MAP News | RSS | 3 — media local |
| Hespress | RSS | 3 — media local |
| Geopolitique.ma | HTML | 3 — media analytique local |

---

## Boost automatique (v2.1)
Les articles sur drones, IA militaire, Maroc-Afrique, FAR, cybersécurité, guerre hybride
remontent automatiquement en tête du digest avec le tag `[>]`.
Configurable dans `BOOST_KEYWORDS` dans [config.py](config.py).

---

## Flux d'exécution

```
[L/M/V 9h] run_digest()
  → scraper.get_articles_for_pole(sources_du_pole, keywords)
  → tri boost → priorité source → max 10 articles
  → storage.save_pending()
  → sender.send_digest()          ← digest Telegram avec [>] sur boostés

[En continu 60s] check_user_commands()
  → sender.get_updates(offset)
  → parse_selection("3" ou "1,3") → max 2 articles
  → generator.generate(article)   ← composition Claude 21 §
  → sender.send(composition)
  → storage.mark_seen()

[Dimanche 20h] send_weekly_planning()
  → message planning semaine à venir
```

---

## Interaction Telegram
- Répondre `3` → composition article 3
- Répondre `1,3` → 2 compositions (article 1 puis article 3)
- Max 2 articles par sélection

---

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

## Règles Absolues Composition
- Phrases courtes (15-25 mots)
- Vocabulaire simple
- IS = Idée abstraite + Fait + Exemple
- Vérifier Limites : Temps / Espace / Domaine
- IM = 1 seule phrase sans point ni point-virgule

---

## Lancer le bot (local — PC, tant qu'il est allumé)
```bash
cd "c:\Users\gameh\Documents\Claude\Projects\Saas Voip\CEM-CG"
python main.py
```

## Déploiement VPS Contabo (24/7 — recommandé)
Le bot tourne en service systemd sur le VPS, à côté des bots trading.
Ressources : ~50 MB RAM idle, ~300 MB pic (chromium headless 3×/sem), ~500 MB disque.

```bash
# 1. SSH sur le VPS
ssh -i ~/.ssh/id_ed25519 freqtrader@157.173.103.9

# 2. Lancer le script de deploiement (clone + venv + playwright + service systemd)
curl -sL https://raw.githubusercontent.com/Gamehdi05/CEM-CG/master/deploy_cem.sh -o /tmp/deploy_cem.sh
bash /tmp/deploy_cem.sh
# (1er passage : il cree /home/freqtrader/cem-cg/.env depuis l'exemple et s'arrete)

# 3. Editer le .env avec les vraies cles, puis relancer
nano /home/freqtrader/cem-cg/.env
bash /tmp/deploy_cem.sh

# Gestion du service
sudo systemctl status cem-cg        # etat
sudo systemctl restart cem-cg       # redemarrer
journalctl -u cem-cg -f             # logs systemd
tail -f /home/freqtrader/cem-cg/bot.log
```

Mise à jour après un push : `cd /home/freqtrader/cem-cg && git pull && sudo systemctl restart cem-cg`
Fichiers de déploiement dans le repo : [cem-cg.service](cem-cg.service), [deploy_cem.sh](deploy_cem.sh)

## GitHub
```
https://github.com/Gamehdi05/CEM-CG
```

---

## Travail réalisé

| Session | Date | Réalisé |
|---------|------|---------|
| S1 | 2026-05 | Clone repo Mehdi-22, config Claude API + Telegram, push Gamehdi05/CEM-CG |
| S2 | 2026-05 | 12 sources (RSS + HTML + Playwright), IRIS/UNECA/Ifri/ISS Africa/IRES/Geopolitique.ma |
| S3 | 2026-05 | v2 : digest thématique + sélection interactive (pending_articles + getUpdates polling) |
| S4 | 2026-05-11 | v2.1 : planning L/M/V, boost militaire/IA [>], planning dimanche 20h. BOT LANCÉ. |
| S5 | 2026-05-12 | fix parse_selection (guillemets) ; fix boost matching (mot entier, retrait IA/AI/FAR) ; déploiement Docker sur VPS Contabo (`/home/freqtrader/cem-cg`, conteneur `cem-cg`, restart unless-stopped). Flux validé : digest → réponse N → composition Claude reçue ✅. |

## Prochaine étape recommandée
Rien d'urgent. Le bot tourne 24/7 sur le VPS. Surveiller le 1er digest automatique
(mercredi 9h — Économie & Développement). Optionnel : passer la branche par défaut
du repo GitHub de `main` à `master` (cf. note plus bas).
