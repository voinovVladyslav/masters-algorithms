import math

from graphs.types import GraphAsDict, CostsDict, ParentsDict


def initialize_single_source(graph: GraphAsDict, start: str) -> tuple[CostsDict, ParentsDict]:
    costs = {}
    parents = {}

    for vertice in graph:
        costs[vertice] = math.inf
        parents[vertice] = None

    costs[start] = 0
    return costs, parents


def bellman_ford(graph: GraphAsDict, start: str, end: str) -> tuple[bool, tuple[str, ...]]:
    def produce_result(parents: ParentsDict, end: str) -> tuple[str, ...]:
        result = [end]
        parent = parents.get(end, None)
        while parent:
            result.append(parent)
            parent = parents.get(parent, None)
        return tuple(result)

    costs, parents = initialize_single_source(graph, start)
    for _ in graph.items():
        for from_vert, vertice in graph.items():
            for to_vert in vertice.keys():
                from_to_cost = graph[from_vert][to_vert]
                if costs[to_vert] > costs[from_vert] + from_to_cost:
                    costs[to_vert] = costs[from_vert] + from_to_cost
                    parents[to_vert] = from_vert


    for from_vert, vertice in graph.items():
        for to_vert in vertice.keys():
            from_to_cost = graph[from_vert][to_vert]
            if costs[to_vert] > costs[from_vert] + from_to_cost:
                return False, None
    return True, produce_result(parents, end)
