from typing import Tuple

# noinspection PyPackageRequirements
from graphics import *


class CustomGraphics:
    def __init__(self, title: str, width: float, height: float) -> None:
        self.width = width
        self.height = height
        self.win = GraphWin(title, width, height)
        self.x, self.y = self._define_origin()

    def draw_point(self, x: float, y: float) -> None:
        x, y = self._translate_points(x, y)
        point = Point(x, y)
        point.draw(self.win)

    def draw_line(self, x_start: float, y_start: float, x_end: float, y_end: float) -> None:
        x_start, y_start = self._translate_points(x_start, y_start)
        x_end, y_end = self._translate_points(x_end, y_end)

        line = Line(Point(x_start, y_start), Point(x_end, y_end))
        line.draw(self.win)

    def _define_origin(self) -> (int, int):
        return self._get_half_width(), self._get_half_height()

    def draw_axis(self) -> None:
        self._draw_y_axis()
        self._draw_x_axis()

    def _draw_y_axis(self) -> None:
        upper_y = self._get_half_width()
        lower_y = -upper_y

        self.draw_line(0, upper_y, 0, lower_y)

    def _draw_x_axis(self) -> None:
        right_x = self._get_half_width()
        left_x = -right_x

        self.draw_line(right_x, 0, left_x, 0)

    def _translate_points(self, x: float, y: float) -> Tuple[float, float]:
        return x + self.x, -y + self.y

    def _get_half_height(self) -> float:
        return self.height/2

    def _get_half_width(self) -> float:
        return self.width/2

    def wait(self) -> None:
        self.win.getMouse()
        self.win.close()


