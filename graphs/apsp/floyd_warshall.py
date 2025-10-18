import math
from typing import Any, TypeAlias

AdjacencyMatrix: TypeAlias = list[list[Any | None]]


def apsp(graph: AdjacencyMatrix) -> tuple[AdjacencyMatrix, AdjacencyMatrix]:
    n = len(graph)
    matrix = [[math.inf for i in range(n)] for j in range(n)]
    predecestors = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            value = graph[i][j]
            if value is None:
                continue
            matrix[i][j] = value
            predecestors[i][j] = i
        matrix[i][i] = 0

    # k is for intermetiate vertex (between i and j)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    predecestors[i][j] = predecestors[k][j]

    return matrix, predecestors


def reconstruct_path(predecessors: AdjacencyMatrix, start: int, end: int):
    if predecessors[start][end] is None:
        return None
    path = [end]
    while end != start:
        end = predecessors[start][end]
        path.append(end)
    return path[::-1]


if __name__ == '__main__':
    _ = None
    graph: AdjacencyMatrix = [
        # a b  c  d  e  f
        [_, 5, 2, _, _, _],  # a
        [1, _, _, _, 3, _],  # b
        [_, -1, _, -5, 3, _],  # c
        [_, _, _, _, _, 0],  # d
        [_, _, 2, 2, _, 9],  # e
        [_, _, _, _, _, _],  # f
    ]
    res, pred = apsp(graph)
    # for row in res:
    #     print(row)

    # for row in pred:
    #     print(row)

    print(reconstruct_path(pred, 0, 1))
