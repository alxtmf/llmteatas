def create_matrix(n):
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()[:n]))
        matrix.append(row)
    return matrix


def swap_diagonals(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i][i], matrix[i][n - i - 1] = matrix[i][n - i - 1], matrix[i][i]
    return matrix

if __name__ == "__main__":
    A = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]
    expected_output = [[5, 2, 3, 4, 1],
                       [6, 9, 8, 7, 10],
                       [11, 12, 13, 14, 15],
                       [16, 19, 18, 17, 20],
                       [25, 22, 23, 24, 21]]
    result = swap_diagonals(A)
    print("Исходная матрица:")
    for row in A:
        print(' '.join(map(str, row)))

    print("Результат:")
    for row in result:
        print(' '.join(map(str, row)))

    if result == expected_output:
        print("Тест пройден")
    else:
        print("Тест не пройден")