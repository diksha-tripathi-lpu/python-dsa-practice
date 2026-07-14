'''Write a Python function that takes two three-dimensional numeric data sets and adds them componentwise.'''

def add_3d_arrays(array1, array2):

    if (len(array1) != len(array2) or
        len(array1[0]) != len(array2[0]) or
        len(array1[0][0]) != len(array2[0][0])):
        print("Arrays must have the same dimensions.")
        return None

    depth = len(array1)
    rows = len(array1[0])
    cols = len(array1[0][0])

    result = []

    for i in range(depth):
        layer = []
        for j in range(rows):
            row = []
            for k in range(cols):
                row.append(array1[i][j][k] + array2[i][j][k])
            layer.append(row)
        result.append(layer)

    return result

array1 = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

array2 = [
    [
        [10, 20],
        [30, 40]
    ],
    [
        [50, 60],
        [70, 80]
    ]
]

result = add_3d_arrays(array1, array2)

print("Resultant 3D Array:")
for layer in result:
    print(layer)