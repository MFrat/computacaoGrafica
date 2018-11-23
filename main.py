import itertools
import time

from core.CustomGraphics import CustomGraphics
from drawing.Figure import Zero3D

graph = CustomGraphics('CG', 500, 500)
graph.draw_axis()

zero = Zero3D(graph)
zero.draw_boundary()
graph.wait()
