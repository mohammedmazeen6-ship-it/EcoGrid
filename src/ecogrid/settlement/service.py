from .models import Settlement

class SettlementService:
    def __init__(self):
        self.settlements = {}

    def settle(self, trade_id, buyer_id, seller_id, amount):
        if trade_id in self.settlements:
            return self.settlements[trade_id]

        if amount < 0:
            raise ValueError("Settlement amount cannot be negative")

        settlement = Settlement(
            trade_id=trade_id,
            buyer_id=buyer_id,
            seller_id=seller_id,
            amount=amount,
            status="COMPLETED",
        )
        self.settlements[trade_id] = settlement
        return settlement
