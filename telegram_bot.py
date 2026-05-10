import time
import logging
from datetime import datetime
import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"


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
