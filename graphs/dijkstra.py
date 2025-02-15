import math

from graphs.types import (
    AdjacencyMatrix,
    Cost,
    CostsDict,
    GraphAsDict,
    Node,
    ParentsDict,
)


def dijkstra(graph: GraphAsDict, start: str, end: str) -> list[str]:
    costs: CostsDict = {}
    for key in graph.keys():
        costs[key] = math.inf
    costs[start] = 0

    parents: ParentsDict = {}
    for key in graph.keys():
        parents[key] = None
    parents.pop(start)

    visited: list[str] = []
    node_name = get_smallest_cost_node(costs, visited)
    while node_name:
        node = graph[node_name]

        for neighbor, cost in node.items():
            current_cost = cost + costs[node_name]

            if current_cost < costs[neighbor]:
                costs[neighbor] = current_cost
                parents[neighbor] = node_name

        visited.append(node_name)
        node_name = get_smallest_cost_node(costs, visited)

    result = [end]
    parent = parents.get(end, None)
    while parent:
        result.append(parent)
        parent = parents.get(parent, None)

    return result


def get_smallest_cost_node(costs: CostsDict, visited: list[str]) -> str | None:
    min_value = math.inf
    min_node = None
    for node_name, value in costs.items():
        if node_name in visited:
            continue

        if value < min_value:
            min_value = value
            min_node = node_name

    return min_node


def dijkstra_raw(graph: AdjacencyMatrix, start: Node, end: Node) -> list[Node]:
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
    node = get_smalled_cost_node_raw(costs, visited)
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
        node = get_smalled_cost_node_raw(costs, visited)

    result = [end]
    parent = parents[end]
    while parent is not None:
        result.append(parent)
        parent = parents[parent]
    return result


def get_smalled_cost_node_raw(
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
