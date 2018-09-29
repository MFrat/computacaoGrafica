import math

from core.motion import transpose_matrix
from core.motion.translation import translation_matrix
from core.motion.matrix import Matrix


def cos(angle):
    return math.cos(math.radians(angle))


def sin(angle):
    return math.sin(math.radians(angle))


def rotation_matrix(angle, center_x=0, center_y=0):
    rot = Matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ])

    pre = Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [-center_x, -center_y, 1]
    ])

    pos = Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [center_x, center_y, 1]
    ])

    return pre, rot, pos


def rotate(angle, path, center_x, center_y):
    rot_matrix = rotation_matrix(angle=angle, center_x=center_x, center_y=center_y)

    path2 = [(i[0] - center_x, i[1] + center_y, i[2]) for i in path]
    path3 = [(Matrix([i]) * rot_matrix)[0] for i in path2]
    return [(i[0] + center_x, i[1] - center_y, 1) for i in path3]
