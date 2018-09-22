import itertools
import time

from core.CustomGraphics import CustomGraphics
from drawing.Figure import Zero

graph = CustomGraphics('CG', 500, 500)
graph.draw_axis()

zero = Zero(position=(300, 300), graph=graph, edge_size=100, name='Zero1')
zero.draw()
zero2 = Zero(position=(100, 150), graph=graph, edge_size=200, name='Zero2')
zero2.draw()
# zero2 = Zero(position=(-100, -100), graph=graph, edge_size=130, name='Zero2')
# zero2.draw()


def rotate(figures):
    for i, j in list(itertools.zip_longest(range(361), range(91))):
        time.sleep(.01)
        if i is not None:
            figures[0].rotate(i)

        if j is not None:
            figures[1].rotate(j)


rotate([zero2, zero])
graph.wait()
