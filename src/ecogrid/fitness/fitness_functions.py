class FitnessFunctions:
    @staticmethod
    def latency_ms(start, end):
        return (end - start) * 1000

    @staticmethod
    def within_latency(start, end, threshold_ms):
        return FitnessFunctions.latency_ms(start, end) <= threshold_ms

    @staticmethod
    def no_duplicate(processed_ids, event_id):
        return processed_ids.count(event_id) <= 1

    @staticmethod
    def security_scan_passed(critical_vulnerabilities):
        return critical_vulnerabilities == 0

    @staticmethod
    def deployment_check(build_ok, tests_ok, security_ok):
        return build_ok and tests_ok and security_ok
