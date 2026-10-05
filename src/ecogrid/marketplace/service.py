from .models import EnergyOffer, EnergyRequest

class MarketplaceService:
    def __init__(self):
        self.offers = {}
        self.requests = {}

    def add_offer(self, offer: EnergyOffer):
        if offer.quantity_kwh <= 0 or offer.price_per_kwh < 0:
            raise ValueError("Invalid offer")
        self.offers[offer.offer_id] = offer

    def add_request(self, request: EnergyRequest):
        if request.quantity_kwh <= 0 or request.max_price_per_kwh < 0:
            raise ValueError("Invalid request")
        self.requests[request.request_id] = request

    def match(self, offer_id, request_id):
        offer = self.offers[offer_id]
        request = self.requests[request_id]

        if offer.price_per_kwh > request.max_price_per_kwh:
            return None

        quantity = min(offer.quantity_kwh, request.quantity_kwh)

        return {
            "type": "TradeCompleted",
            "offer_id": offer.offer_id,
            "request_id": request.request_id,
            "seller_id": offer.seller_id,
            "buyer_id": request.buyer_id,
            "quantity_kwh": quantity,
            "price_per_kwh": offer.price_per_kwh,
            "total_amount": round(quantity * offer.price_per_kwh, 2),
        }
