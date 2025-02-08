import math

from graphs.types import GraphAsDict, CostsDict, ParentsDict


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
