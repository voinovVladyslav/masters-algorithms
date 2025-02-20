from graphs.search import calculate_bellman_ford
from graphs.types import AdjacencyMatrix

_ = None
# Dijkstra
# graph: AdjacencyMatrix = [
#     # a  b  c  d  e  f
#     [_, 1, 5, 10, _, _],  # a
#     [_, _, 13, _, _, _],  # b
#     [_, _, _, _, 2, _],  # c
#     [_, _, 1, _, _, 12],  # d
#     [_, _, _, _, _, 5],  # e
#     [_, _, _, _, _, _],  # f
# ]

# Bellman Ford
graph: AdjacencyMatrix = [
    # a b  c  d  e  f
    [_, 5, 2, _, _, _],  # a
    [1, _, _, _, 3, _],  # b
    [_, -1, _, -5, 3, _],  # c
    [_, _, _, _, _, 0],  # d
    [_, _, 2, 2, _, 9],  # e
    [_, _, _, _, _, _],  # f
]
# Bellman Ford, negative cycle
# graph: AdjacencyMatrix = [
#     # a b  c  d  e  f
#     [_, 5, 2, _, _, _],  # a
#     [1, _, _, _, -3, _],  # b
#     [_, -1, _, -5, 3, _],  # c
#     [_, 1, _, -2, 5, 0],  # d
#     [_, _, 2, 2, _, 9],  # e
#     [_, _, _, _, _, _],  # f
# ]


print(calculate_bellman_ford(graph, 0, 5))
