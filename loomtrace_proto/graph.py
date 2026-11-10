"""Provenance graph built from span probes."""


class TraceGraph:
    def __init__(self, spans):
        self.spans = spans

    @classmethod
    def from_probe(cls, probe) -> "TraceGraph":
        return cls(spans=probe.collect())

    def rank_suspects(self, method: str = "pagerank"):
        return {"method": method, "nodes": len(self.spans)}
