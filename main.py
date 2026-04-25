import argparse
import logging

from dotenv import load_dotenv

from src.scheduler import run_scheduler, send_daily_report

load_dotenv()

LOG_FORMAT: str = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
logger: logging.Logger = logging.getLogger(__name__)


def configure_logging() -> None:
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Send the Telegram sales report once or keep the in-process scheduler running."
    )
    parser.add_argument(
        "--loop",
        action="store_true",
        help="Keep the Python scheduler running instead of sending one report and exiting.",
    )
    return parser.parse_args()


def main() -> None:
    configure_logging()
    args = parse_args()

    try:
        if args.loop:
            logger.info("Starting in scheduler loop mode")
            run_scheduler()
        else:
            logger.info("Starting in one-time run mode")
            send_daily_report()
    except Exception as e:
        logger.exception("Application failed: %s", e)
        raise SystemExit(1)

if __name__ == "__main__":
    main()
