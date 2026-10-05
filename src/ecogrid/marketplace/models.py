from dataclasses import dataclass

@dataclass
class EnergyOffer:
    offer_id: str
    seller_id: str
    quantity_kwh: float
    price_per_kwh: float

@dataclass
class EnergyRequest:
    request_id: str
    buyer_id: str
    quantity_kwh: float
    max_price_per_kwh: float
