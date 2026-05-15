import json
import hashlib
import unicodedata
import re
import logging
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = Path("data/seen_topics.json")
PENDING_FILE = Path("data/pending_articles.json")
OFFSET_FILE = Path("data/update_offset.json")
ARCHIVE_FILE = Path("data/compositions.md")


def _normalize(text: str) -> str:
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text.strip()


class Storage:
    def __init__(self):
        DATA_FILE.parent.mkdir(exist_ok=True)
        if not DATA_FILE.exists():
            DATA_FILE.write_text("{}")
        self._data = self._load()

    def _load(self) -> dict:
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}

    def _save(self):
        DATA_FILE.write_text(json.dumps(self._data, ensure_ascii=False, indent=2), encoding="utf-8")

    @staticmethod
    def hash(title: str) -> str:
        return hashlib.sha256(_normalize(title).encode()).hexdigest()[:16]

    def is_seen(self, topic_hash: str) -> bool:
        return topic_hash in self._data

    def mark_seen(self, topic_hash: str, title: str, url: str):
        self._data[topic_hash] = {
            "title": title,
            "url": url,
            "seen_at": datetime.utcnow().isoformat(),
        }
        self._save()

    def cleanup_old_entries(self, days: int = 30):
        cutoff = datetime.utcnow() - timedelta(days=days)
        before = len(self._data)
        self._data = {
            k: v for k, v in self._data.items()
            if datetime.fromisoformat(v["seen_at"]) > cutoff
        }
        removed = before - len(self._data)
        if removed:
            logging.info(f"Cleanup: {removed} entrees supprimees")
            self._save()

    def save_pending(self, articles: list[dict]):
        numbered = {str(i + 1): a for i, a in enumerate(articles)}
        PENDING_FILE.write_text(
            json.dumps(numbered, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def load_pending(self) -> dict:
        if not PENDING_FILE.exists():
            return {}
        try:
            return json.loads(PENDING_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}

    def save_update_offset(self, offset: int):
        OFFSET_FILE.write_text(
            json.dumps({"offset": offset}), encoding="utf-8"
        )

    def load_update_offset(self) -> int:
        if not OFFSET_FILE.exists():
            return 0
        try:
            return json.loads(OFFSET_FILE.read_text(encoding="utf-8")).get("offset", 0)
        except Exception:
            return 0

    def migrate_seen_to_archive(self):
        if ARCHIVE_FILE.exists():
            return
        entries = sorted(self._data.items(), key=lambda x: x[1].get("seen_at", ""))
        lines = ["# Archive des Compositions CEM-CG\n"]
        for _, v in entries:
            date_str = v.get("seen_at", "")[:16].replace("T", " ")
            lines.append(
                f"\n---\n\n"
                f"## {date_str} — {v.get('title', 'Sans titre')}\n"
                f"**URL** : {v.get('url', '')}\n\n"
                f"*Composition generee avant l'archivage automatique (v2.2) — texte non disponible.*\n"
            )
        ARCHIVE_FILE.write_text("".join(lines), encoding="utf-8")
        logging.info(f"Migration archive: {len(entries)} sujets existants importes dans compositions.md")

    def append_to_archive(self, article: dict, composition: str):
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
        if not ARCHIVE_FILE.exists():
            ARCHIVE_FILE.write_text("# Archive des Compositions CEM-CG\n", encoding="utf-8")
        entry = (
            f"\n---\n\n"
            f"## {date_str} — {article.get('title', 'Sans titre')}\n"
            f"**Source** : {article.get('source', '')}\n"
            f"**URL** : {article.get('url', '')}\n\n"
            f"{composition}\n"
        )
        with ARCHIVE_FILE.open("a", encoding="utf-8") as f:
            f.write(entry)
        logging.info(f"Composition archivee: {article.get('title', '')[:60]}")
