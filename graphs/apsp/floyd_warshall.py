import math

from graphs.types import AdjacencyMatrix


# TODO: compute predecestor matrix along with asps matrix
def apsp(graph: AdjacencyMatrix) -> AdjacencyMatrix:
    n = len(graph)
    matrix = [[math.inf for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            value = graph[i][j]
            if value is None:
                continue
            matrix[i][j] = value

    # k is for intermetiate vertex (between i and j)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    matrix[i][j] = 0
                    continue
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    return matrix
