class EventBus:
    def __init__(self):
        self.subscribers = {}
        self.processed_events = set()

    def subscribe(self, event_type, handler):
        self.subscribers.setdefault(event_type, []).append(handler)

    def publish(self, event_id, event):
        if event_id in self.processed_events:
            return []

        self.processed_events.add(event_id)
        event_type = event["type"]
        results = []

        for handler in self.subscribers.get(event_type, []):
            results.append(handler(event))

        return results
