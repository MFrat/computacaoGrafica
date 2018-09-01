from typing import Tuple, List

from core.CustomGraphics import CustomGraphics

Point = Tuple[float, float]


class Figure:
    def __init__(self, path: List[Point], name: str = '', width: float = 500, height: float =500) -> None:
        self.path = path
        self.graph = CustomGraphics(title=name, width=width, height=height)

    def draw(self) -> None:
        for i in range(len(self.path)-1):
            self._draw_line(self.path[i], self.path[i+1])

        self.graph.wait()

    def _draw_line(self, point_start: Tuple[float, float], point_end: Tuple[float, float]) -> None:
        self.graph.draw_line('green', *point_start, *point_end)

    def draw_axis(self):
        self.graph.draw_axis()


class Zero(Figure):
    def __init__(self, position: Tuple[float, float] = (0, 0), edge_size: float = 100,
                 name: str = 'Zero', width: float = 500, height: float = 500) -> None:
        self.position = position
        self.edge_size = edge_size
        super().__init__(self._get_vertexes(), name, width, height)

    def _get_vertexes(self) -> List[Point]:
        x, y = self.position
        right_top = (x, y)
        left_top = (x + self.edge_size, y)
        right_bot = (x, y - self.edge_size)
        left_bot = (x + self.edge_size, y - self.edge_size)

        l = [right_top, left_top, left_bot, right_bot]

        return l + [l[0]]
