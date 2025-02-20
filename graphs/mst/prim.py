from typing import NamedTuple

from graphs.types import AdjacencyMatrix, Cost, Node


class Vertice(NamedTuple):
    name: Node
    cost: Cost
    parent: Node | None


def minimum_spanning_tree(
    graph: AdjacencyMatrix, start: int = 0
) -> AdjacencyMatrix:
    graph_size = len(graph)
    return graph
