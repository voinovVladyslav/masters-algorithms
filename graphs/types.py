from typing import Any, TypeAlias

Vertice: TypeAlias = dict[str, int]
GraphAsDict: TypeAlias = dict[str, Vertice]
CostsDict: TypeAlias = dict[str, int | float]
ParentsDict: TypeAlias = dict[str, str | None]


Node: TypeAlias = int
Cost: TypeAlias = Any
AdjacencyMatrix: TypeAlias = list[list[Cost | None]]
