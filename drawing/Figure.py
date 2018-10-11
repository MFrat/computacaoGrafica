from typing import Tuple, List

from core.CustomGraphics import CustomGraphics
from core.motion.rotation import rotate
from core.motion.translation import translation

Point = Tuple[float, float]


class Figure:
    def __init__(self, graph: CustomGraphics, position, width, height, rotation_center=None, name: str = None) -> None:
        if graph is None:
            raise ValueError('Graph can not be None')

        if rotation_center is not None and len(rotation_center) != 2:
            raise ValueError('Rotation center must be a list or tuple with length 2')

        self.position = position
        self.width = width
        self.height = height
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

    def translate(self, delta):
        # TODO, ao inves de passar o delte, passar a posição final.
        self.erase()
        self.draw(custom_path=translation(x_delta=delta, y_delta=delta, path=self.path))

    def rotate(self, angle, delta=0):
        self.erase()
        self.draw(custom_path=rotate(angle, self.path, self.rotation_center_x, -self.rotation_center_y, delta))

    def get_rotation_center(self):
        return self.rotation_center_x, self.rotation_center_y

    @property
    def rotation_center_x(self):
        if self._rotation_center_x is None:
            self._rotation_center_x = self.x + self.width/2
            return self._rotation_center_x

        return self._rotation_center_x

    @property
    def rotation_center_y(self):
        if self._rotation_center_y is None:
            self._rotation_center_y = self.y - self.height/2
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
    def __init__(self, height, width, graph: CustomGraphics, position = (0, 0), name = None, rotation_center=None) -> None:

        self._path = None
        super().__init__(graph=graph, position=position, width=width, height=height, name=name, rotation_center=rotation_center)

    def _get_vertexes(self) -> List[Point]:
        x, y = self.position
        right_top = (x, y, 1)
        left_top = (x + self.width, y, 1)
        right_bot = (x, y - self.height, 1)
        left_bot = (x + self.width, y - self.height, 1)

        l = [right_top, right_top, right_bot, right_bot, left_bot, left_bot, left_top, left_top]

        return l + [l[0]]

class _Zero2(Figure):
    def __init__(self, width, height, graph: CustomGraphics, position: Tuple[float, float] = (0, 0), name: str = None) -> None:

        self._path = None
        super().__init__(graph=graph, position=position, width=width, height=height, name=name)

    def _get_vertexes(self) -> List[Point]:
        x, y = self.position
        a = (x, y, 1)
        b = (a[0]+self.width, a[1], 1)
        c = (b[0]+self.width/2, b[1]-self.width/2, 1)
        d = (c[0], c[1]-self.height, 1)
        e = (d[0]-self.width/2, d[1]-self.width/2, 1)
        f = (e[0]-self.width, e[1], 1)
        g = (f[0]-self.width/2, f[1]+self.width/2, 1)
        h = (g[0], g[1]+self.height, 1)

        l = [a, b, c, d, e, f, g, h]

        return l + [l[0]]


class Zero:
    def __init__(self, graph: CustomGraphics, position: Tuple[float, float] = (0, 0),
                 edge_size: float = 100, name: str = None) -> None:
        self.position = position
        zero2 = _Zero2(position=position, graph=graph, width=10, height=20, name='{0}1'.format(name if name is not None else 'Zero'))
        zero = _Zero(position=(position[0], position[1]-5), graph=graph, height=20, width=10, 
                     name='{0}2'.format(name if name is not None else 'Zero'), rotation_center=zero2.get_rotation_center())
        self.parts = [
            zero2, zero
        ]

    def draw(self) -> None:
        for i in self.parts:
            i.draw()

    def update_position(self, new_pos):
        self.parts[0].update_position(new_pos)
        self.parts[1].update_position((new_pos[0]+10, new_pos[1]-10))

    def rotate(self, angle, delta):
        for i in self.parts:
            i.rotate(angle, delta)

    def translate(self, delta):
        for i in self.parts:
            i.translate(delta)

    def erase(self) -> None:
        for i in self.parts:
            i.erase()
