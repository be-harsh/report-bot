import csv
import logging
from datetime import date
from pathlib import Path
from typing import Generator

from src.models import SaleRecord

logger: logging.Logger = logging.getLogger(__name__)

def read_sales_data(file_path: Path) -> Generator[SaleRecord, None, None]:
    """Read the sales CSV file and yield one record at a time."""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row.
            for row in reader:
                date_str, product, quantity, price = row
                sale_date: date = date.fromisoformat(date_str)
                item_quantity: int = int(quantity)
                item_price: float = float(price)
                yield SaleRecord(sale_date, product, item_quantity, item_price)
    except FileNotFoundError:
        logger.error("File not found: %s", file_path)
    except csv.Error as e:
        logger.error("CSV format error: %s", e)
    except ValueError as e:
        logger.error("Data format error: %s", e)

