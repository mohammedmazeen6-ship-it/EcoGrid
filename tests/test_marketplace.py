import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import unittest
from ecogrid.marketplace.models import EnergyOffer, EnergyRequest
from ecogrid.marketplace.service import MarketplaceService


class TestMarketplace(unittest.TestCase):
    def test_matching(self):
        service = MarketplaceService()
        service.add_offer(EnergyOffer("o1", "seller", 5, 0.20))
        service.add_request(EnergyRequest("r1", "buyer", 2, 0.25))
        trade = service.match("o1", "r1")
        self.assertEqual(trade["quantity_kwh"], 2)
        self.assertEqual(trade["total_amount"], 0.40)


if __name__ == "__main__":
    unittest.main()
