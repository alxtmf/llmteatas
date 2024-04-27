def swap_diagonals(matrix):
    N = len(matrix)
    for i in range(N):
        matrix[i][i], matrix[i][N-i-1] = matrix[i][N-i-1], matrix[i][i]

def test_swap_diagonals():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    original_matrix = [row[:] for row in matrix]

    swap_diagonals(matrix)

    for i in range(len(matrix)):
        if matrix[i][i] != original_matrix[i][len(matrix)-i-1] or matrix[i][len(matrix)-i-1] != original_matrix[i][i]:
            return False
    return True

if __name__ == "__main__":
    
    if test_swap_diagonals():
        print("Тест пройден")
    else:
        print("Тест не пройден")