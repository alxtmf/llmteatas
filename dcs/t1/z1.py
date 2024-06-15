# "Дана целочисленная матрица A(N, N). Запишите на место отрицательных
# элементов матрицы нули, а на место положительных - единицы. Матрицу напечатайте в
# общепринятом виде."

def transform_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 0:
                matrix[i][j] = 0
            elif matrix[i][j] > 0:
                matrix[i][j] = 1
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def print_test_result(input_matrix, expected_matrix):
    result = transform_matrix(input_matrix)
    print("Исходная матрица:")
    print_matrix(input_matrix)
    print("Ожидаемая матрица:")
    print_matrix(expected_matrix)
    print("Фактическая матрица:")
    print_matrix(result)
    print("Результат теста:", "Прошел" if result == expected_matrix else "Не прошел")
    print()

matrix1 = [
[4, -2, 3, 1, -6],
[0, 5, -1, 2, 3],
[-7, 8, -3, 0, 9],
[4, -2, 1, 5, -8],
[3, 7, -4, 6, -1]
]

expected_matrix1 = [
[1, 0, 1, 1, 0],
[0, 1, 0, 1, 1],
[0, 1, 0, 0, 1],
[1, 0, 1, 1, 0],
[1, 1, 0, 1, 0]
]

print_test_result(matrix1, expected_matrix1)

matrix2 = [
[-1, -2, -3],
[0, 0, 0],
[1, 2, 3]
]

expected_matrix2 = [
[0, 0, 0],
[0, 0, 0],
[1, 1, 1]
]

print_test_result(matrix2, expected_matrix2)

matrix3 = [
[0, -1, 1],
[1, -1, 0],
[-1, 1, 0]
]

expected_matrix3 = [
[0, 0, 1],
[1, 0, 0],
[0, 1, 0]
]

print_test_result(matrix3, expected_matrix3)