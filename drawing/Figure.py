from typing import Tuple, List

from core.CustomGraphics import CustomGraphics
from core.motion.rotation import rotate

Point = Tuple[float, float]


class Figure:
    def __init__(self, graph: CustomGraphics, position, edge_size, rotation_center=None, name: str = None) -> None:
        if graph is None:
            raise ValueError('Graph can not be None')

        if rotation_center is not None and len(rotation_center) != 2:
            raise ValueError('Rotation center must be a list or tuple with length 2')

        self.position = position
        self.edge_size = edge_size
        self.graph = graph
        self.name = name

        if rotation_center is not None:
            self._rotation_center_x = rotation_center[0]
            self._rotation_center_y = rotation_center[1]
        else:
            self._rotation_center_x = None
            self._rotation_center_y = None

        self._path = None
        self._old_path = None

    def draw(self, custom_path=None, homogeneous=True) -> None:
        p = custom_path if custom_path is not None else self.path
        p = [i[:-1] for i in p if len(i) == 3] if homogeneous else p # Removendo coordenada homogenea
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
        self.erase()
        self.draw(custom_path=rotate(angle, self.path, self.rotation_center_x, -self.rotation_center_y))

    @property
    def rotation_center_x(self):
        if self._rotation_center_x is None:
            self._rotation_center_x = self.x + self.edge_size / 2
            return self._rotation_center_x

        return self._rotation_center_x

    @property
    def rotation_center_y(self):
        if self._rotation_center_y is None:
            self._rotation_center_y = self.y - self.edge_size/2
            return self._rotation_center_y

        return self._rotation_center_y

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    @property
    def path(self):
        if self._path is not None:
            return self._path

        self._path = self._get_vertexes()
        if self._path is None:
            raise ValueError('Path can not be None')

        return self._path

    def _get_vertexes(self) -> List[Point]:
        return []


class _Zero(Figure):
    def __init__(self, graph: CustomGraphics, position: Tuple[float, float] = (0, 0),
                 edge_size: float = 100, name: str = None) -> None:

        self._path = None
        super().__init__(graph=graph, position=position, edge_size=edge_size, name=name)

    def _get_vertexes(self) -> List[Point]:
        x, y = self.position
        right_top = (x, y, 1)
        left_top = (x + self.edge_size, y, 1)
        right_bot = (x, y - self.edge_size, 1)
        left_bot = (x + self.edge_size, y - self.edge_size, 1)

        l = [right_top, left_top, left_bot, right_bot]

        return l + [l[0]]


class Zero:
    def __init__(self, graph: CustomGraphics, position: Tuple[float, float] = (0, 0),
                 edge_size: float = 100, name: str = None) -> None:
        self.position = position
        self.parts = [
            _Zero(position=position, graph=graph, edge_size=edge_size,
                  name='{0}1'.format(name if name is not None else 'Zero')),
            _Zero(position=(position[0]+10, position[1]-10), graph=graph,
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
