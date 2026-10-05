import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import unittest
from ecogrid.events.event_bus import EventBus


class TestEventBus(unittest.TestCase):
    def test_duplicate_event_is_ignored(self):
        bus = EventBus()
        received = []

        bus.subscribe("TestEvent", lambda event: received.append(event))
        event = {"type": "TestEvent", "value": 1}

        bus.publish("event-1", event)
        bus.publish("event-1", event)

        self.assertEqual(len(received), 1)


if __name__ == "__main__":
    unittest.main()
