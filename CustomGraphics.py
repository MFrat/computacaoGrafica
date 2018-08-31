from graphics import *


def _define_origin(win):
    return win.width/2, win.height/2


class CustomGraphics:
    def __init__(self, title, width, height) -> None:
        self.width = width
        self.height = height
        self.win = GraphWin(title, width, height)
        self.x, self.y = _define_origin(self.win)

    def draw_point(self, x: int, y: int):
        x, y = self.translate_points(x, y)
        point = Point(x, y)
        point.draw(self.win)

    def draw_line(self, x_start: int, y_start: int, x_end: int, y_end: int):
        x_start, y_start = self.translate_points(x_start, y_start)
        x_end, y_end = self.translate_points(x_end, y_end)

        line = Line(Point(x_start, y_start), Point(x_end, y_end))
        line.draw(self.win)

    def translate_points(self, x: int, y: int):
        return x + self.x, -y + self.y

    def wait(self):
        self.win.getMouse()
        self.win.close()


