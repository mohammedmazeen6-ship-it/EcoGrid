import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import unittest
from ecogrid.settlement.service import SettlementService


class TestSettlement(unittest.TestCase):
    def test_idempotent_settlement(self):
        service = SettlementService()
        first = service.settle("t1", "buyer", "seller", 1.0)
        second = service.settle("t1", "buyer", "seller", 1.0)
        self.assertIs(first, second)
        self.assertEqual(len(service.settlements), 1)


if __name__ == "__main__":
    unittest.main()
