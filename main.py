
from graphs.utils import graph_to_dict
from graphs.dijkstra import dijkstra

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

print(dijkstra(graph_to_dict(graph), 'A', 'F'))
