# Defining a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print(matrix[0])     
print(matrix[1][2])  


# Matrix addition
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Adding the matrices
result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

print("Matrix addition result:")
for row in result:
    print(row)


# Matrix multiplication
matrix1 = [
    [1, 2],
    [3, 4]
]

matrix2 = [
    [5, 6],
    [7, 8]
]

# Multiplying the matrices
result = [[0, 0], [0, 0]]

for i in range(len(matrix1)):     
    for j in range(len(matrix2[0])):  
        for k in range(len(matrix2)):  
            result[i][j] += matrix1[i][k] * matrix2[k][j]

print("Matrix multiplication result:")
for row in result:
    print(row)


# Transposing a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print("Transposed matrix:")
for row in transpose:
    print(row)

# Matrix Operation


