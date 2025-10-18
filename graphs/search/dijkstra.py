import math

from graphs.types import AdjacencyMatrix, Cost, Node


def calculate_dijkstra(
    graph: AdjacencyMatrix, start: Node, end: Node
) -> list[Node]:
    """
    Graph as adjacency matrix
    """
    costs: list[Cost] = []
    parents: list[Node | None] = []
    for _ in range(len(graph)):
        costs.append(math.inf)
        parents.append(None)

    costs[start] = 0

    visited: list[Node] = []
    node = get_smalled_cost_node(costs, visited)
    while node is not None:
        edges = graph[node]

        for neighbor, cost in enumerate(edges):
            if cost is None:
                continue
            current_cost = cost + costs[node]

            if current_cost < costs[neighbor]:
                costs[neighbor] = current_cost
                parents[neighbor] = node

        visited.append(node)
        node = get_smalled_cost_node(costs, visited)

    result = [end]
    parent = parents[end]
    while parent is not None:
        result.append(parent)
        parent = parents[parent]
    return result


def get_smalled_cost_node(
    costs: list[Cost], visited: list[Node]
) -> Node | None:
    min_value = math.inf
    min_node = None
    for node, cost in enumerate(costs):
        if node in visited:
            continue

        if cost < min_value:
            min_value = cost
            min_node = node

    return min_node
