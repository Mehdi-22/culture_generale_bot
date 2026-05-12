import time
import logging
from datetime import datetime
import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
API_BASE = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"


class TelegramSender:
    def format_message(self, article: dict, composition: str) -> str:
        return (
            f"NOUVEAU SUJET - CULTURE GENERALE\n"
            f"Source: {article.get('source', '')}\n"
            f"{article.get('title', '')}\n"
            f"{article.get('url', '')}\n\n"
            f"COMPOSITION - Methode de Composition\n"
            f"{composition}\n\n"
            f"Genere le {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        )

    def split_message(self, text: str, max_length: int = 4000) -> list[str]:
        if len(text) <= max_length:
            return [text]
        chunks = []
        while text:
            if len(text) <= max_length:
                chunks.append(text)
                break
            cut = text.rfind("\n\n", 0, max_length)
            if cut == -1:
                cut = text.rfind("\n", 0, max_length)
            if cut == -1:
                cut = text.rfind(" ", 0, max_length)
            if cut == -1:
                cut = max_length
            chunks.append(text[:cut].strip())
            text = text[cut:].strip()
        return chunks

    def send(self, message: str) -> bool:
        chunks = self.split_message(message)
        total = len(chunks)
        success = True
        for i, chunk in enumerate(chunks):
            text = f"[Partie {i + 1}/{total}]\n\n{chunk}" if total > 1 else chunk
            try:
                resp = requests.post(
                    BASE_URL,
                    json={"chat_id": TELEGRAM_CHAT_ID, "text": text},
                    timeout=15,
                )
                resp.raise_for_status()
                logging.info(f"Message {i + 1}/{total} envoye")
            except Exception as e:
                logging.error(f"Echec envoi chunk {i + 1}: {e}")
                success = False
            if i < total - 1:
                time.sleep(1.5)
        return success

    def send_digest(self, pole: str, articles: list[dict]) -> bool:
        date_str = datetime.now().strftime("%A %d %B %Y — %Hh%M")
        lines = [f"DIGEST — {pole}", date_str, ""]
        for i, a in enumerate(articles, 1):
            prefix = "[>] " if a.get("_boost") else "    "
            lines.append(f"{prefix}{i}. {a['title']}")
            lines.append(f"       {a.get('source', '')}")
            lines.append("")
        lines.append("Reponds avec le numero pour generer la composition.")
        lines.append("Ex : 3   ou   1,6   (2 max)")
        return self.send("\n".join(lines))

    def get_updates(self, offset: int) -> list[dict]:
        try:
            resp = requests.get(
                f"{API_BASE}/getUpdates",
                params={"offset": offset, "timeout": 0, "limit": 50},
                timeout=10,
            )
            resp.raise_for_status()
            data = resp.json()
            if data.get("ok"):
                return data.get("result", [])
        except Exception as e:
            logging.warning(f"getUpdates erreur: {e}")
        return []

    def parse_selection(self, text: str) -> list[int]:
        # Garde uniquement chiffres et virgules (l'utilisateur tape souvent "1" ou "1,6"
        # avec guillemets en recopiant l'exemple du digest)
        import re
        cleaned = re.sub(r"[^0-9,]", "", text)
        numbers = []
        for part in cleaned.split(","):
            if part.isdigit():
                n = int(part)
                if 1 <= n <= 10:
                    numbers.append(n)
        return numbers[:2]
