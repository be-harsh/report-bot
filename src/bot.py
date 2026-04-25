import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()

logger: logging.Logger = logging.getLogger(__name__)

def send_report(message: str) -> bool:
    """Send the report message to Telegram."""

    token: str | None = os.getenv("BOT_TOKEN")
    chat_id: str | None = os.getenv("CHAT_ID")

    if not token or not chat_id:
        logger.error("Missing BOT_TOKEN or CHAT_ID in environment")
        return False

    url: str = f"https://api.telegram.org/bot{token}/sendMessage"

    try:
        response = requests.get(
            url,
            params={"chat_id": chat_id, "text": message},
            timeout=15,
        )
        response.raise_for_status()
        logger.info("Telegram message sent successfully")
        return True
    except requests.exceptions.RequestException as e:
        logger.error("Error sending message: %s", e)
        return False
    except Exception as e:
        logger.exception("Unexpected error while sending Telegram message: %s", e)
        return False
