import string


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


graph = [
    # a  b  c  d  e  f  g  h
    [0, 1, 1, 0, 0, 0, 0, 0],  # a
    [1, 0, 0, 1, 1, 0, 0, 0],  # b
    [1, 0, 0, 0, 0, 1, 1, 0],  # c
    [0, 1, 0, 0, 0, 0, 0, 1],  # d
    [0, 1, 0, 0, 0, 0, 0, 1],  # e
    [0, 0, 1, 0, 0, 0, 0, 1],  # f
    [0, 0, 1, 0, 0, 0, 0, 1],  # g
    [0, 0, 0, 1, 1, 1, 1, 0],  # g
]

display_graph(graph)
