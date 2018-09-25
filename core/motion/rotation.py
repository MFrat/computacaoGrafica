import math

from core.motion import transpose_matrix
from core.motion.matrix import Matrix


def cos(angle):
    return math.cos(math.radians(angle))


def sin(angle):
    return math.sin(math.radians(angle))


def rotation_matrix(angle):
    return Matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ])

def cu(angle=0):
    return Matrix([
        [1, 0, angle],
        [0, 1, angle],
        [0, 0, 1]
    ])


def rotate(angle, path, center_x, center_y):
    rot_matrix = rotation_matrix(angle)

    path2 = [(i[0] - center_x, i[1] + center_y, i[2]) for i in path]
    path3 = [(Matrix([i]) * rot_matrix * cu())[0] for i in path2]
    path4 = [(i[0] + center_x, i[1] - center_y, 1) for i in path3]
    aux = [(i[0] + center_x, i[1] - center_y, 1) for i in Matrix(Matrix(path2) * rot_matrix).get_matrix()]

    # aaaa = [transpose_matrix([i]) for i in path]
    # print(aaaa)
    # path4 = [transpose_matrix(cu(angle) * Matrix(i))[0] for i in aaaa]
    # print(path4)
    return aux
