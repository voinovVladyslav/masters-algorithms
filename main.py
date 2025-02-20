from pprint import pprint

from graphs.mst.kruskal import minimum_spanning_tree as kruskal
from graphs.mst.prim import minimum_spanning_tree as prim
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
# graph: AdjacencyMatrix = [
#     # a b  c  d  e  f
#     [_, 5, 2, _, _, _],  # a
#     [1, _, _, _, 3, _],  # b
#     [_, -1, _, -5, 3, _],  # c
#     [_, _, _, _, _, 0],  # d
#     [_, _, 2, 2, _, 9],  # e
#     [_, _, _, _, _, _],  # f
# ]
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

graph: AdjacencyMatrix = [
    # 0 1  2  3  4
    [_, 5, 1, _, _],  # 0
    [5, _, 8, 9, 3],  # 1
    [1, 8, _, _, 8],  # 2
    [_, 9, _, _, 5],  # 3
    [_, 3, 8, 5, _],  # 4
]


pprint(prim(graph))
pprint(kruskal(graph))
