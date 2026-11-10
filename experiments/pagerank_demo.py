from loomtrace_proto.probes import SpanProbe
from loomtrace_proto.graph import TraceGraph


if __name__ == "__main__":
    probe = SpanProbe(service="checkout", sample_rate=0.2)
    graph = TraceGraph.from_probe(probe)
    print(graph.rank_suspects(method="pagerank"))
