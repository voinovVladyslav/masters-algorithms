import string

from graphs.types import GraphAsDict


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
