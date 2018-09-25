def transpose_matrix(matrix):
    return [i for i in map(list, zip(*matrix))]
