import math
from typing import Any, TypeAlias

Node: TypeAlias = int
Cost: TypeAlias = Any
AdjacencyMatrix: TypeAlias = list[list[Cost | None]]


def calculate_dijkstra(
    graph: AdjacencyMatrix, start: Node, end: Node
) -> list[Node]:
    # initialize costs, where list index is name of the node
    # and value is actual cost
    costs: list[Cost] = []

    # initialize costs, where list index is name of the node
    # and value is actual cost
    parents: list[Node | None] = []
    for _ in range(len(graph)):
        costs.append(math.inf)
        parents.append(None)

    # set cost to 0 for starting node
    costs[start] = 0

    visited: list[Node] = []
    # get smallest unvisited node
    node = get_smalled_cost_node(costs, visited)
    # while there is unvisited nodes
    while node is not None:
        edges = graph[node]

        for neighbor, cost in enumerate(edges):
            if cost is None:
                continue
            current_cost = cost + costs[node]

            # update cost if it's lower than already known cost
            if current_cost < costs[neighbor]:
                costs[neighbor] = current_cost
                parents[neighbor] = node

        # mark node as visited
        visited.append(node)
        # get next smallest unvisited node
        node = get_smalled_cost_node(costs, visited)

    result = [end]
    parent = parents[end]
    while parent is not None:
        result.append(parent)
        parent = parents[parent]
    return result[::-1]


def get_smalled_cost_node(
    costs: list[Cost], visited: list[Node]
) -> Node | None:
    """Find smallest unvisited node"""
    min_value = math.inf
    min_node = None
    for node, cost in enumerate(costs):
        if node in visited:
            continue

        if cost < min_value:
            min_value = cost
            min_node = node

    return min_node


if __name__ == '__main__':
    _ = None
    # Dijkstra
    graph: AdjacencyMatrix = [
        # a  b  c  d  e  f
        [_, 1, 5, 10, _, _],  # a
        [_, _, 13, _, _, _],  # b
        [_, _, _, _, 2, _],  # c
        [_, _, 1, _, _, 12],  # d
        [_, _, _, _, _, 5],  # e
        [_, _, _, _, _, _],  # f
    ]
    # find shortest path from first to last node
    result = calculate_dijkstra(graph, 0, 5)
    print(result)
