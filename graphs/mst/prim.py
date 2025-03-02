import math

from graphs.types import AdjacencyMatrix, Cost, Node


def minimum_spanning_tree(
    graph: AdjacencyMatrix, start: int = 0
) -> AdjacencyMatrix:
    graph_size = len(graph)
    costs: list[Cost] = [math.inf] * graph_size
    parents: list[Node | None] = [None] * graph_size
    in_mst: list[bool] = [False] * graph_size

    costs[start] = 0

    # print('costs:', costs)
    for _ in range(graph_size):
        available_costs = [
            (costs[v], v) for v in range(graph_size) if in_mst[v] is False
        ]
        # print('available_costs:', available_costs)

        u = min(available_costs)[1]
        in_mst[u] = True
        # print('is_mst:', in_mst)

        for v in range(graph_size):
            if (
                graph[u][v] is not None
                and in_mst[v] is False
                and graph[u][v] < costs[v]
            ):
                costs[v] = graph[u][v]
                parents[v] = u
                # print('u:', u, 'v:', v)
                # print('costs:', costs)
                # print('parents:', parents)

        # print()

    result = [[None for j in range(graph_size)] for i in range(graph_size)]
    for node, p in enumerate(parents):
        if p is None:
            continue
        result[node][p] = graph[node][p]
        result[p][node] = graph[p][node]

    return result
