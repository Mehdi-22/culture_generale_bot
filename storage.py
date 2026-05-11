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
