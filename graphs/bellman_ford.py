import math

from graphs.types import (
    AdjacencyMatrix,
    Cost,
    CostsDict,
    GraphAsDict,
    Node,
    ParentsDict,
)


def initialize_single_source(
    graph: GraphAsDict, start: str
) -> tuple[CostsDict, ParentsDict]:
    costs: CostsDict = {}
    parents: ParentsDict = {}

    for vertice in graph:
        costs[vertice] = math.inf
        parents[vertice] = None

    costs[start] = 0
    return costs, parents


def produce_result(parents: ParentsDict, end: str) -> tuple[str, ...]:
    result = [end]
    parent = parents.get(end, None)
    while parent:
        result.append(parent)
        parent = parents.get(parent, None)
    return tuple(result)


def bellman_ford(
    graph: GraphAsDict, start: str, end: str
) -> tuple[bool, tuple[str, ...] | None]:
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


def produce_result_new(parents: list[Node | None], end: int) -> tuple[int, ...]:
    result = [end]
    parent = parents[end]
    while parent is not None:
        result.append(parent)
        parent = parents[parent]
    return tuple(result)

def initialize_single_source_new(
    graph: AdjacencyMatrix, start: int
) -> tuple[list[Cost], list[Node | None]]:
    parents: list[Node | None] = [None] * len(graph)
    costs: list[Cost] = [math.inf] * len(graph)
    costs[start] = 0
    return costs, parents


def bellman_ford_new(
    graph: AdjacencyMatrix, start: int, end: int
) -> tuple[bool, tuple[int, ...] | None]:
    costs, parents = initialize_single_source_new(graph, start)
    for _ in range(len(graph)):
        for from_vert, vertice in enumerate(graph):
            for to_vert, cost in enumerate(vertice):
                if cost is None:
                    continue

                if costs[to_vert] > costs[from_vert] + cost:
                    costs[to_vert] = costs[from_vert] + cost
                    parents[to_vert] = from_vert

    for from_vert, vertice in enumerate(graph):
        for to_vert, cost in enumerate(vertice):
            if cost is None:
                continue

            if costs[to_vert] > costs[from_vert] + cost:
                return False, None

    return True, produce_result_new(parents, end)
