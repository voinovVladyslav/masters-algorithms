from graphs.utils import graph_to_dict
from graphs.bellman_ford import bellman_ford

# graph = [
#     # a  b  c  d  e  f
#     [0, 1, 0, 10, 0, 0],  # a
#     [0, 0, 13, 0, 0, 0],  # b
#     [0, 0, 0, 0, 2, 0],  # c
#     [0, 0, 1, 0, 0, 12],  # d
#     [0, 0, 0, 0, 0, 5],  # e
#     [0, 0, 0, 0, 0, 0],  # f
# ]

_ = None
# graph = [
#     # a b  c  d  e  f
#     [_, 5, 2, _, _, _],  # a
#     [1, _, _, _, 3, _],  # b
#     [_, -1, _, -5, 3, _],  # c
#     [_, _, _, _, _, 0],  # d
#     [_, _, 2, 2, _, 9],  # e
#     [_, _, _, _, _, _],  # f
# ]
graph = [
    # a b  c  d  e  f
    [_, 5, 2, _, _, _],  # a
    [1, _, _, _, 3, _],  # b
    [_, -1, _, -5, 3, _],  # c
    [_, _, _, _, 5, 0],  # d
    [_, _, 2, 2, _, 9],  # e
    [_, _, _, _, _, _],  # f
]

# print(graph_to_dict(graph))

print(bellman_ford(graph_to_dict(graph), "A", "F"))
