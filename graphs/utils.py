import string

from graphs.types import AdjacencyMatrix, GraphAsDict


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


def display_graph(graph: AdjacencyMatrix, start: int = 0) -> None:
    print('   ' + ''.join(f'{x:^3}' for x in range(start, len(graph) + start)))
    for i, row in enumerate(graph, start):
        print(f'{i:<3}', end='')
        for value in row:
            display = value
            if value is None:
                display = '_'
            print(f'{display:^3}', end='')
        print()


def graph_to_dict(graph: list[list[int | None]]) -> GraphAsDict:
    nodes = len(graph)
    new_graph: GraphAsDict = {}
    for i in range(nodes):
        parent_name = get_node_name(i)
        new_graph[parent_name] = {}
        for j in range(nodes):
            if (value := graph[i][j]) is None:
                continue
            child_name = get_node_name(j)
            new_graph[parent_name][child_name] = value

    return new_graph
