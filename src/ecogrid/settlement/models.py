from dataclasses import dataclass

@dataclass
class Settlement:
    trade_id: str
    buyer_id: str
    seller_id: str
    amount: float
    status: str
