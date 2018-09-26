import time
from core.motion import transpose_matrix
from core.motion.matrix import Matrix

def _translation_matrix(x_delta=0, y_delta=0):
    return Matrix([
        [1, 0, x_delta],
        [0, 1, y_delta],
        [0, 0, 1]
    ])

def translation(x_delta, y_delta, path):
    matrix = _translation_matrix(x_delta, y_delta)
    transposed_matrix = [transpose_matrix([i]) for i in path]
    return [transpose_matrix(matrix * Matrix(i))[0] for i in transposed_matrix]
