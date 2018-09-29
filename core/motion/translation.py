import time
from core.motion import transpose_matrix
from core.motion.matrix import Matrix

def translation_matrix(x_delta=0, y_delta=0):
    return Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [x_delta, y_delta, 1]
    ])

def translation(x_delta, y_delta, path):
    matrix = translation_matrix(x_delta, y_delta)
    return [(Matrix([i]) * matrix)[0] for i in path]
