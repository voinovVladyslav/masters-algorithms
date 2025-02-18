from typing import Any, TypeAlias

Vertice: TypeAlias = dict[str, int]
GraphAsDict: TypeAlias = dict[str, Vertice]

Node: TypeAlias = int
Cost: TypeAlias = Any
AdjacencyMatrix: TypeAlias = list[list[Cost | None]]
