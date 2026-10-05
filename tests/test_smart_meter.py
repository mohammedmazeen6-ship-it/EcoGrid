import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import unittest
from ecogrid.smart_meter.service import SmartMeterService


class TestSmartMeter(unittest.TestCase):
    def test_excess_energy(self):
        event = SmartMeterService().ingest("m1", 10, 6, 1)
        self.assertEqual(event["excess_kwh"], 4)

    def test_negative_energy_rejected(self):
        with self.assertRaises(ValueError):
            SmartMeterService().ingest("m1", -1, 2, 1)


if __name__ == "__main__":
    unittest.main()
