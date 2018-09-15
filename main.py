import time

from core.CustomGraphics import CustomGraphics
from drawing.Figure import Zero

graph = CustomGraphics('CG', 500, 500)
graph.draw_axis()

zero = Zero(position=(100, 100), graph=graph, edge_size=100, name='Zero1')
zero.draw()
zero2 = Zero(position=(-100, -100), graph=graph, edge_size=100, name='Zero2')
zero2.draw()

time.sleep(3)

zero.erase()

graph.wait()
