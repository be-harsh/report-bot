import logging
import time

import schedule

from config import SALES_FILE, SCHEDULE_TIME
from src.analyzer import analyze_sales
from src.bot import send_report
from src.formatter import format_report
from src.reader import read_sales_data

logger: logging.Logger = logging.getLogger(__name__)


def send_daily_report() -> None:
    """Run the full report flow and send the result to Telegram."""

    try:
        sales_file = SALES_FILE
        sales_data = list(read_sales_data(sales_file))
        report = analyze_sales(sales_data)
        formatted_report: str = format_report(report)
        result: bool = send_report(formatted_report)
        if result:
            logger.info("Daily report sent successfully")
        else:
            logger.error("Failed to send daily report")
    except Exception as e:
        logger.exception("Error while sending daily report: %s", e)

def run_scheduler() -> None:
    """Keep the Python scheduler running and send the report every day."""

    schedule.every().day.at(SCHEDULE_TIME).do(send_daily_report)
    logger.info("Scheduler started for daily run at %s", SCHEDULE_TIME)
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    try:
        run_scheduler()
    except Exception as e:
        logger.exception("Scheduler stopped due to an error: %s", e)
        raise SystemExit(1)

