import math

from core.motion.matrix import Matrix


def cos(angle):
    return math.cos(math.radians(angle))


def sin(angle):
    return math.sin(math.radians(angle))


def rotation_matrix(angle):
    return Matrix([
        [cos(angle), -sin(angle)],
        [sin(angle), cos(angle)]
    ])


def rotate(angle, path, center_x, center_y):
    rot_matrix = rotation_matrix(angle)

    path2 = [(i[0] - center_x, i[1] + center_y) for i in path]
    return [(i[0] + center_x, i[1] - center_y) for i in Matrix(Matrix(path2) * rot_matrix).get_matrix()]
