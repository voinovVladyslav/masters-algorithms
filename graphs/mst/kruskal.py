from dataclasses import dataclass

from graphs.types import AdjacencyMatrix


@dataclass(frozen=True)
class Edge:
    from_vertice: int
    to_vertice: int
    cost: int | float

    def __eq__(self, other) -> bool:
        same_cost = self.cost == other.cost
        same_path = (
            self.from_vertice == other.from_vertice
            and self.to_vertice == other.to_vertice
        )
        reversed_path = (
            self.from_vertice == other.to_vertice
            and self.to_vertice == other.from_vertice
        )
        return same_cost and (same_path or reversed_path)


def find_set(vertice: int, sets: list[set[int]]) -> set[int]:
    for s in sets:
        if vertice in s:
            return s

    raise ValueError(f'Invalid vertice {vertice}')


def minimum_spanning_tree(graph: AdjacencyMatrix) -> AdjacencyMatrix:
    """
    find minimum spanning tree using Kruskal's algorithm
    weight of mst can be calculated by sum of weights under diagonal
    """
    size = len(graph)
    edges: list[Edge] = []
    for from_vertice in range(size):
        for to_vertice in range(size):
            cost = graph[from_vertice][to_vertice]
            if cost is None:
                continue
            edge = Edge(
                from_vertice=from_vertice, to_vertice=to_vertice, cost=cost
            )
            if edge in edges:
                continue
            edges.append(edge)
    edges = sorted(edges, key=lambda obj: obj.cost)

    mst_edges: list[Edge] = []
    forest = [{i} for i in range(size)]
    for edge in edges:
        s1 = find_set(edge.from_vertice, forest)
        s2 = find_set(edge.to_vertice, forest)
        if s1 == s2:
            continue

        forest.pop(forest.index(s1))
        forest.pop(forest.index(s2))
        forest.append(s1.union(s2))
        mst_edges.append(edge)

    result: AdjacencyMatrix = [[None for j in range(size)] for i in range(size)]
    for edge in mst_edges:
        result[edge.from_vertice][edge.to_vertice] = edge.cost
        result[edge.to_vertice][edge.from_vertice] = edge.cost

    return result
