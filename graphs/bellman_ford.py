import math

from graphs.types import AdjacencyMatrix, Cost, Node


def produce_result(parents: list[Node | None], end: int) -> tuple[int, ...]:
    result = [end]
    parent = parents[end]
    while parent is not None:
        result.append(parent)
        parent = parents[parent]
    return tuple(result)


def initialize_single_source(
    graph: AdjacencyMatrix, start: int
) -> tuple[list[Cost], list[Node | None]]:
    parents: list[Node | None] = [None] * len(graph)
    costs: list[Cost] = [math.inf] * len(graph)
    costs[start] = 0
    return costs, parents


def bellman_ford(
    graph: AdjacencyMatrix, start: int, end: int
) -> tuple[bool, tuple[int, ...] | None]:
    costs, parents = initialize_single_source(graph, start)
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

    return True, produce_result(parents, end)
