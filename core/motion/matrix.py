class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix = matrix

    def __mul__(self, other):
        return self.multiply(other, self._init_matrix(len(other[0]), len(self.matrix)))

    def __rmul__(self, other):
        return self.multiply(other, self._init_matrix(len(self.matrix), len(other[0])))

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def _init_matrix(self, len1, len2):
        return [[0 for _ in range(len1)] for _ in range(len2)]

    def multiply(self, other, result):
        for i in range(len(self.matrix)):
            for j in range(len(other[0])):
                for k in range(len(other)):
                    result[i][j] += self.matrix[i][k] * other[k][j]

        return result

    def __str__(self):
        return '\n'.join([''.join(['{:10}'.format(item) for item in row]) for row in self.matrix])


mat1 = Matrix([[12, 7, 3], [4, 5, 6], [7, 8, 9]])
mat2 = Matrix([[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]])
print(Matrix(mat1 * mat2))
