import time

from core.CustomGraphics import CustomGraphics
from core.motion.matrix import Matrix
from core.motion.rotation import sin, cos
from drawing.Figure import Zero

graph = CustomGraphics('CG', 500, 500)
graph.draw_axis()

zero = Zero(position=(0, 0), graph=graph, edge_size=100, name='Zero1')
zero.draw()
# zero2 = Zero(position=(-100, -100), graph=graph, edge_size=130, name='Zero2')
# zero2.draw()

time.sleep(1)
for i in range(361):
    time.sleep(.05)
    zero.rotate(i)

graph.wait()
