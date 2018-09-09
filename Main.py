from core.CustomGraphics import CustomGraphics
from drawing.Figure import Zero

graph = CustomGraphics('CG', 500, 500)

graph.draw_axis()

zero = Zero(position=(30, 30), graph=graph, edge_size=100)
zero2 = Zero(position=(40, 20), graph=graph, edge_size=80)

zero.draw()
zero2.draw()

graph.wait()
