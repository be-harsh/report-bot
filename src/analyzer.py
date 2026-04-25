from collections import Counter
import logging
from datetime import date

from src.models import ReportSummary, SaleRecord

logger = logging.getLogger(__name__)


def analyze_sales(sales_records: list[SaleRecord]) -> ReportSummary:
    try:
        if not sales_records:
            raise ValueError("No sales records provided")
        
        total_revenue = sum(record.total_price for record in sales_records)
        total_orders = len(sales_records)
        product_count = Counter(record.product for record in sales_records)
        top_product = product_count.most_common(1)[0][0] if product_count else "N/A"
        average_order_value = total_revenue / total_orders if total_orders > 0 else 0
        report_date = date.today().strftime("%d-%B-%Y")
        
        return ReportSummary(
            total_revenue=total_revenue,
            total_orders=total_orders,
            top_product=top_product,
            average_order_value=average_order_value,
            report_date=report_date
        )
    except ValueError as e:
        logger.error("Sales analysis failed: %s", e)
        raise

