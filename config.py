from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR: Path = Path(__file__).resolve().parent
DATA_DIR: Path = BASE_DIR / "data"
SALES_FILE: Path = DATA_DIR / "sales.csv"
BOT_TOKEN: str | None = os.getenv("BOT_TOKEN")
CHAT_ID: str | None = os.getenv("CHAT_ID")
SCHEDULE_TIME: str = "09:00"

