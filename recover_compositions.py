#!/usr/bin/env python3
"""
Script one-shot : recupere les compositions depuis l'historique Telegram
et les ajoute dans data/compositions.md.

Prerequis :
  pip install telethon python-dotenv
  Obtenir API_ID et API_HASH sur https://my.telegram.org (section "API development tools")

Usage :
  python recover_compositions.py
"""

import asyncio
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv()

CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID", "0"))
ARCHIVE_FILE = Path("data/compositions.md")

# Marque le debut d'un message de composition envoye par le bot
COMP_MARKER = "NOUVEAU SUJET - CULTURE GENERALE"


def parse_composition_message(text: str) -> dict | None:
    """Extrait metadonnees + texte d'un message de composition du bot."""
    # Retire le prefixe [Partie N/N] si le message a ete coupe
    text = re.sub(r"^\[Partie \d+/\d+\]\n\n", "", text.strip())

    if COMP_MARKER not in text:
        return None

    lines = text.split("\n")
    source = ""
    title = ""
    url = ""
    comp_lines = []
    in_comp = False

    for i, line in enumerate(lines):
        if line.startswith("Source: "):
            source = line[8:].strip()
        elif line.startswith("http") and not url:
            url = line.strip()
        elif line == "COMPOSITION - Methode de Composition":
            in_comp = True
            # La ligne precedente non-vide est le titre
            for prev in reversed(lines[:i]):
                if prev.strip() and not prev.startswith("http") and not prev.startswith("Source:") and COMP_MARKER not in prev:
                    title = prev.strip()
                    break
        elif in_comp:
            if line.startswith("Genere le "):
                break
            comp_lines.append(line)

    composition = "\n".join(comp_lines).strip()

    if not title or not composition:
        return None

    return {
        "title": title,
        "source": source,
        "url": url,
        "composition": composition,
    }


async def main():
    try:
        from telethon import TelegramClient
    except ImportError:
        print("Telethon non installe. Lance d'abord :")
        print("  pip install telethon")
        sys.exit(1)

    if not CHAT_ID:
        print("TELEGRAM_CHAT_ID manquant dans .env")
        sys.exit(1)

    print("=== Recuperation compositions Telegram ===")
    print()
    print("Obtiens ton API_ID et API_HASH sur https://my.telegram.org")
    print("(section 'API development tools')")
    print()
    api_id_str = input("API_ID : ").strip()
    api_hash = input("API_HASH : ").strip()

    if not api_id_str or not api_hash:
        print("API_ID et API_HASH requis.")
        sys.exit(1)

    api_id = int(api_id_str)

    client = TelegramClient("session_recovery", api_id, api_hash)
    await client.start()

    print(f"\nConnecte. Recuperation des messages du chat {CHAT_ID}...")

    raw_messages = []
    async for message in client.iter_messages(CHAT_ID, limit=None):
        if message.text:
            raw_messages.append((message.date, message.text))

    await client.disconnect()

    print(f"{len(raw_messages)} messages recuperes. Analyse...")

    # Trier chronologiquement
    raw_messages.sort(key=lambda x: x[0])

    # Les messages longs sont envoyes en plusieurs parties consecutives.
    # On regroupe les parties [Partie N/N] en un seul texte.
    merged = []
    i = 0
    while i < len(raw_messages):
        date, text = raw_messages[i]
        part_match = re.match(r"^\[Partie (\d+)/(\d+)\]", text)
        if part_match:
            total = int(part_match.group(2))
            combined = re.sub(r"^\[Partie \d+/\d+\]\n\n", "", text)
            for j in range(1, total):
                if i + j < len(raw_messages):
                    next_text = raw_messages[i + j][1]
                    combined += "\n" + re.sub(r"^\[Partie \d+/\d+\]\n\n", "", next_text)
            merged.append((date, combined))
            i += total
        else:
            merged.append((date, text))
            i += 1

    # Extraire les compositions
    compositions = []
    for date, text in merged:
        parsed = parse_composition_message(text)
        if parsed:
            parsed["msg_date"] = date.strftime("%Y-%m-%d %H:%M")
            compositions.append(parsed)

    if not compositions:
        print("Aucune composition trouvee dans l'historique.")
        return

    print(f"{len(compositions)} composition(s) trouvees.")

    # Charger les titres deja dans l'archive pour eviter les doublons
    existing_titles: set[str] = set()
    if ARCHIVE_FILE.exists():
        content = ARCHIVE_FILE.read_text(encoding="utf-8")
        for match in re.finditer(r"^## .+? — (.+)$", content, re.MULTILINE):
            existing_titles.add(match.group(1).strip())
    else:
        ARCHIVE_FILE.write_text("# Archive des Compositions CEM-CG\n", encoding="utf-8")

    added = 0
    with ARCHIVE_FILE.open("a", encoding="utf-8") as f:
        for comp in compositions:
            if comp["title"] in existing_titles:
                print(f"  (deja present) {comp['title'][:80]}")
                continue
            entry = (
                f"\n---\n\n"
                f"## {comp['msg_date']} — {comp['title']}\n"
                f"**Source** : {comp['source']}\n"
                f"**URL** : {comp['url']}\n\n"
                f"{comp['composition']}\n"
            )
            f.write(entry)
            existing_titles.add(comp["title"])
            added += 1
            print(f"  + {comp['title'][:80]}")

    print(f"\n{added} composition(s) ajoutee(s) dans {ARCHIVE_FILE}")
    if Path("session_recovery.session").exists():
        Path("session_recovery.session").unlink()
        print("Fichier de session supprime.")


if __name__ == "__main__":
    asyncio.run(main())
