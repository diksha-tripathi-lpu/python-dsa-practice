'''Write a Python program for a matrix class that can add and multiply two-dimensional arrays of numbers, assuming the dimensions agree appropriately for the operation.'''

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, other):

        if (len(self.matrix) != len(other.matrix) or
            len(self.matrix[0]) != len(other.matrix[0])):
            print("Matrices must have the same dimensions for addition.")
            return None

        rows = len(self.matrix)
        cols = len(self.matrix[0])

        result = []

        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)

        return Matrix(result)

    def multiply(self, other):

        if len(self.matrix[0]) != len(other.matrix):
            print("Matrix multiplication is not possible.")
            return None

        rows = len(self.matrix)
        cols = len(other.matrix[0])
        common = len(other.matrix)

        result = []

        for i in range(rows):
            row = []
            for j in range(cols):
                total = 0
                for k in range(common):
                    total += self.matrix[i][k] * other.matrix[k][j]
                row.append(total)
            result.append(row)

        return Matrix(result)

    def display(self):
        for row in self.matrix:
            print(row)


matrix1 = Matrix([
    [1, 2],
    [3, 4]
])

matrix2 = Matrix([
    [5, 6],
    [7, 8]
])

print("Matrix Addition:")
addition = matrix1.add(matrix2)
if addition:
    addition.display()

print("\nMatrix Multiplication:")
multiplication = matrix1.multiply(matrix2)
if multiplication:
    multiplication.display()