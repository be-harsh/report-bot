from src.models import ReportSummary


def format_report(report: ReportSummary) -> str:
    """Build the Telegram message in a simple text format."""

    return f"""
    {"="*50}
    Daily Sales Report - {report.report_date}
    Total Revenue: ₹{report.total_revenue:.2f}
    Total Orders: {report.total_orders}
    Top Product: {report.top_product}
    Average Order Value: ₹{report.average_order_value:.2f}
    {"="*50}
    """

