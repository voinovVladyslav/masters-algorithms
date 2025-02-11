from typing import TypeAlias


Vertice: TypeAlias = dict[str, int]
GraphAsDict: TypeAlias = dict[str, Vertice]
CostsDict: TypeAlias = dict[str, int | float]
ParentsDict: TypeAlias = dict[str, str | None]
