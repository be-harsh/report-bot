from dataclasses import dataclass
from datetime import date


@dataclass
class SaleRecord:
    sale_date: date
    product: str
    quantity: int
    price: float

    @property
    def total_price(self) -> float:
        return self.quantity * self.price

@dataclass
class ReportSummary:
    total_revenue: float
    total_orders: int
    top_product: str
    average_order_value: float
    report_date: date
