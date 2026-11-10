"""Span probes for microservice meshes."""


class SpanProbe:
    def __init__(self, service: str, sample_rate: float = 0.1):
        self.service = service
        self.sample_rate = sample_rate

    def collect(self):
        return [{"service": self.service, "op": "checkout"}]
