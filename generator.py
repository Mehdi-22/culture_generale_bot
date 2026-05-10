import time
import logging
import anthropic
from config import ANTHROPIC_API_KEY, CLAUDE_MODEL
from prompts.methode import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE


class CompositionGenerator:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    def generate(self, article: dict) -> str | None:
        prompt = USER_PROMPT_TEMPLATE.format(
            title=article.get("title", ""),
            source=article.get("source", ""),
            summary=article.get("summary", ""),
            url=article.get("url", ""),
        )
        for attempt in range(3):
            try:
                message = self.client.messages.create(
                    model=CLAUDE_MODEL,
                    max_tokens=4000,
                    system=SYSTEM_PROMPT,
                    messages=[{"role": "user", "content": prompt}],
                )
                return message.content[0].text
            except anthropic.RateLimitError as e:
                logging.error(f"Tentative {attempt + 1} echouee (rate limit): {e}")
                if attempt < 2:
                    time.sleep(2 ** (attempt + 1))
            except anthropic.APIError as e:
                logging.error(f"Tentative {attempt + 1} echouee (API): {e}")
                if attempt < 2:
                    time.sleep(2 ** attempt)
        return None
