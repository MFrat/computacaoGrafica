from typing import Tuple, List

from core.CustomGraphics import CustomGraphics
from core.motion.matrix import Matrix
from core.motion.rotation import sin, cos

Point = Tuple[float, float]


class Figure:
    def __init__(self, graph: CustomGraphics, position, name: str = None) -> None:
        if graph is None:
            raise ValueError('Graph can not be None')
        self.position = position

        if self.path is None:
            raise ValueError('Path can not be None')

        self.graph = graph
        self.name = name

        self._path = None

    def draw(self, custom_path=None) -> None:
        p = custom_path if custom_path is not None else self.path

        for i in range(len(p) - 1):
            self._draw_line(p[i], p[i + 1])

    def erase(self):
        self.graph.erase(self.name)

    def move(self, x, y):
        self.graph.move(self.name, x, y)

    def update_position(self, new_pos):
        self.move(new_pos[0]-self.position[0], -(new_pos[1]-self.position[1]))
        self.position = new_pos

    def _draw_line(self, point_start: Tuple[float, float], point_end: Tuple[float, float]) -> None:
        self.graph.draw_line('green', *point_start, *point_end, obj_id=self.name)

    def rotate(self, angle):
        rotation_matrix = Matrix([
            [cos(angle), -sin(angle)],
            [sin(angle), cos(angle)]
        ])

        self.erase()
        self.draw(custom_path=Matrix(Matrix(self.path)*rotation_matrix).get_matrix())

    @property
    def path(self):
        if self._path is not None:
            return self._path

        self._path = self._get_vertexes()
        return self._path

    def _get_vertexes(self) -> List[Point]:
        return []


class _Zero(Figure):
    def __init__(self, graph: CustomGraphics, position: Tuple[float, float] = (0, 0),
                 edge_size: float = 100, name: str = None) -> None:
        self.edge_size = edge_size

        self._path = None
        super().__init__(graph, position, name)

    def _get_vertexes(self) -> List[Point]:
        x, y = self.position
        right_top = (x, y)
        left_top = (x + self.edge_size, y)
        right_bot = (x, y - self.edge_size)
        left_bot = (x + self.edge_size, y - self.edge_size)

        l = [right_top, left_top, left_bot, right_bot]

        return l + [l[0]]


class Zero:
    def __init__(self, graph: CustomGraphics, position: Tuple[float, float] = (0, 0),
                 edge_size: float = 100, name: str = None) -> None:
        self.position = position
        self.parts = [
            _Zero(position=position, graph=graph, edge_size=edge_size,
                  name='{0}1'.format(name if name is not None else 'Zero')),
            _Zero(position=(position[0]+10, position[0]-10), graph=graph,
                  edge_size=edge_size-20, name='{0}2'.format(name if name is not None else 'Zero'))
        ]

    def draw(self) -> None:
        for i in self.parts:
            i.draw()

    def update_position(self, new_pos):
        self.parts[0].update_position(new_pos)
        self.parts[1].update_position((new_pos[0]+10, new_pos[1]-10))

    def rotate(self, angle):
        for i in self.parts:
            i.rotate(angle)

    def erase(self) -> None:
        for i in self.parts:
            i.erase()
