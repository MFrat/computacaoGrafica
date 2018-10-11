import itertools
import time

from core.CustomGraphics import CustomGraphics
from drawing.Figure import Zero

graph = CustomGraphics('CG', 500, 500)
graph.draw_axis()

zero = Zero(position=(50, 50), graph=graph, edge_size=10, name='Zero1')
zero.draw()
# zero2 = Zero(position=(100, 100), graph=graph, edge_size=100, name='Zero2')
# zero2.draw()
# zero2 = Zero(position=(-100, -100), graph=graph, edge_size=130, name='Zero2')
# zero2.draw()

time.sleep(1)


def rotate(figures):
    angles = range(91)
    translation = range(51)
    for angle, pos in list(itertools.zip_longest(angles, translation)):
        #time.sleep(.01)
        angle = angle if angle is not None else 90
        pos = pos if pos is not None else 50
        figures[0].rotate(angle, pos)
        # figures[1].rotate(angle, pos)
        # if j is not None:
        #     figures[1].translate(j)


# for i in range(10000):
#     zero.rotate(i)


rotate([zero])
graph.wait()
