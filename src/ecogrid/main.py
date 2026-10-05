import time

from smart_meter.service import SmartMeterService
from marketplace.models import EnergyOffer, EnergyRequest
from marketplace.service import MarketplaceService
from settlement.service import SettlementService
from events.event_bus import EventBus
from fitness.fitness_functions import FitnessFunctions


def main():
    meter = SmartMeterService()
    marketplace = MarketplaceService()
    settlement = SettlementService()
    bus = EventBus()

    def handle_meter(event):
        if event["excess_kwh"] > 0:
            marketplace.add_offer(
                EnergyOffer(
                    offer_id=f"offer-{event['meter_id']}",
                    seller_id=event["meter_id"],
                    quantity_kwh=event["excess_kwh"],
                    price_per_kwh=0.25,
                )
            )
        return event

    def handle_trade(event):
        return settlement.settle(
            trade_id=event["offer_id"] + "-" + event["request_id"],
            buyer_id=event["buyer_id"],
            seller_id=event["seller_id"],
            amount=event["total_amount"],
        )

    bus.subscribe("MeterReadingValidated", handle_meter)
    bus.subscribe("TradeCompleted", handle_trade)

    start = time.perf_counter()

    meter_event = meter.ingest("meter-001", 8.0, 5.0, time.time())
    bus.publish("meter-event-001", meter_event)

    marketplace.add_request(
        EnergyRequest(
            request_id="request-001",
            buyer_id="home-002",
            quantity_kwh=2.0,
            max_price_per_kwh=0.30,
        )
    )

    trade = marketplace.match("offer-meter-001", "request-001")
    settlement_result = bus.publish("trade-event-001", trade)

    end = time.perf_counter()

    print("Meter Event:", meter_event)
    print("Trade:", trade)
    print("Settlement:", settlement_result)
    print("Latency ms:", round(FitnessFunctions.latency_ms(start, end), 3))


if __name__ == "__main__":
    main()
