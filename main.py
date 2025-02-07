import math
import string

GraphAsDict = dict[str, dict[str, int]]
CostsDict = dict[str, int | float]
ParentsDict = dict[str, str | None]


def get_node_name(number: int) -> str:
    """
    Returns number equivalent as alphabet name

    Examples:
    `0` -> `"A"`
    `4` -> `"E"`
    `25` -> `"Z"`
    `26` -> `"AA"`
    """
    first, last = divmod(number, 26)
    if not first:
        return string.ascii_uppercase[last]
    return string.ascii_uppercase[first - 1] + string.ascii_uppercase[last]


def display_graph(graph: list[list]) -> None:
    nodes = len(graph)
    for i in range(nodes):
        node_name = get_node_name(i)
        vertices = []
        for j in range(nodes):
            if graph[i][j]:
                vertices.append(get_node_name(j))
        print(node_name, vertices)


def graph_to_dict(graph: list[list[int]]) -> GraphAsDict:
    nodes = len(graph)
    new_graph: GraphAsDict = {}
    for i in range(nodes):
        parent_name = get_node_name(i)
        new_graph[parent_name] = {}
        for j in range(nodes):
            if not (value := graph[i][j]):
                continue
            child_name = get_node_name(j)
            new_graph[parent_name][child_name] = value

    return new_graph


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


graph = [
    # a  b  c  d  e  f
    [0, 1, 0, 10, 0, 0],  # a
    [0, 0, 13, 0, 0, 0],  # b
    [0, 0, 0, 0, 2, 0],  # c
    [0, 0, 1, 0, 0, 12],  # d
    [0, 0, 0, 0, 0, 5],  # e
    [0, 0, 0, 0, 0, 0],  # f
]
print(graph_to_dict(graph))

# print(dijkstra(graph_to_dict(graph), 'A', 'F'))
