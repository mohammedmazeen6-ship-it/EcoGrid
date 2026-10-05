class RetryPolicy:
    def __init__(self, max_retries=3):
        self.max_retries = max_retries

    def execute(self, operation):
        last_error = None
        for _ in range(self.max_retries + 1):
            try:
                return operation()
            except Exception as exc:
                last_error = exc
        raise last_error


class CircuitBreaker:
    def __init__(self, failure_threshold=3):
        self.failure_threshold = failure_threshold
        self.failures = 0
        self.open = False

    def call(self, operation):
        if self.open:
            raise RuntimeError("Circuit breaker is open")

        try:
            result = operation()
            self.failures = 0
            return result
        except Exception:
            self.failures += 1
            if self.failures >= self.failure_threshold:
                self.open = True
            raise
