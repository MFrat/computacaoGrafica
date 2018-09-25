import time
from core.motion import transpose_matrix
from core.motion.matrix import Matrix

def _translation_matrix(x_delta=0, y_delta=0):
    return Matrix([
        [1, 0, x_delta],
        [0, 1, y_delta],
        [0, 0, 1]
    ])

def translation(pos_start, pos_end, path):
    aaaa = [transpose_matrix([i]) for i in path]
    print(aaaa)
    path4 = [transpose_matrix(_translation_matrix() * Matrix(i))[0] for i in aaaa]
    print(path4)
