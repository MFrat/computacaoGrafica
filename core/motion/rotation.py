import math

from core.motion.matrix import Matrix


def cos(angle):
    return math.cos(math.radians(angle))


def sin(angle):
    return math.sin(math.radians(angle))


# angle = 45
# rotation_matrix = Matrix([
#     [cos(angle), -sin(angle)],
#     [sin(angle), cos(angle)]
# ])
# l2 = Matrix([
#     (200, 200),
#     (300, 200),
#     (300, 100),
#     (200, 100)
# ])
# print(Matrix(l2*rotation_matrix))
