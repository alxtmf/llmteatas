"""В целочисленной матрице A(N, N) найдите для каждой строки число
элементов, кратных пяти, и наибольший из полученных результатов."""

import numpy as np
import unittest


def matrix_multiples(matrix):
    return np.max(np.sum(matrix % 5 == 0, axis=1))


class TestMatrixMultiples(unittest.TestCase):
    def test_regular_matrix(self):
        matrix = np.array(
            [[5, 10, 15, 20], [1, 2, 3, 4], [25, 30, 35, 40], [5, 6, 7, 8]]
        )
        self.assertEqual(matrix_multiples(matrix), 4)

    def test_no_multiples_of_five(self):
        matrix = np.array(
            [[1, 2, 3, 4], [6, 7, 8, 9], [11, 12, 13, 14], [16, 17, 18, 19]]
        )
        self.assertEqual(matrix_multiples(matrix), 0)

    def test_all_multiples_of_five(self):
        matrix = np.array(
            [[5, 10, 15, 20], [25, 30, 35, 40], [45, 50, 55, 60], [65, 70, 75, 80]]
        )
        self.assertEqual(matrix_multiples(matrix), 4)

    def test_single_row_multiple_of_five(self):
        matrix = np.array([[1, 2, 3, 4], [5, 10, 15, 20], [1, 2, 3, 4], [1, 2, 3, 4]])
        self.assertEqual(matrix_multiples(matrix), 4)

    def test_empty_matrix(self):
        matrix = np.array([[]])
        self.assertEqual(matrix_multiples(matrix), 0)


if __name__ == "__main__":
    unittest.main()
