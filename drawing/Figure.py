from typing import Tuple, List

from core.CustomGraphics import CustomGraphics

Point = Tuple[float, float]


class Figure:
    def __init__(self, graph: CustomGraphics) -> None:
        if graph is None:
            raise ValueError('Graph can not be None')

        self.path = self._get_vertexes()

        if self.path is None:
            raise ValueError('Path can not be None')

        self.graph = graph

    def draw(self) -> None:
        for i in range(len(self.path) - 1):
            self._draw_line(self.path[i], self.path[i + 1])

    def _draw_line(self, point_start: Tuple[float, float], point_end: Tuple[float, float]) -> None:
        self.graph.draw_line('green', *point_start, *point_end)

    def _get_vertexes(self) -> List[Point]:
        return []


class Zero(Figure):
    def __init__(self, graph: CustomGraphics, position: Tuple[float, float] = (0, 0),
                 edge_size: float = 100) -> None:
        self.position = position
        self.edge_size = edge_size
        super().__init__(graph)

    def _get_vertexes(self) -> List[Point]:
        x, y = self.position
        right_top = (x, y)
        left_top = (x + self.edge_size, y)
        right_bot = (x, y - self.edge_size)
        left_bot = (x + self.edge_size, y - self.edge_size)

        l = [right_top, left_top, left_bot, right_bot]

        return l + [l[0]]
