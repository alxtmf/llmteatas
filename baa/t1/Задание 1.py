def create_matrix(n):
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()[:n]))
        matrix.append(row)
    return matrix

def swap_diagonals(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i][i], matrix[i][n-i-1] = matrix[i][n-i-1], matrix[i][i]
    return matrix

N = int(input("Введите размер матрицы: "))

print("Введите элементы:")
A = create_matrix(N)

print("Исходная матрица:")
for row in A:
    print(' '.join(map(str, row)))

result = swap_diagonals(A)

print("Результат:")
for row in result:
    print(' '.join(map(str, row)))
import time
time.sleep(5)