"""Написать функцию, которая вычисляет количество
нулевых элементов одномерного массива."""

import numpy as np
import unittest


def zero_counting(array):
    return np.sum(np.array(array) == 0)


class TestZeroCounting(unittest.TestCase):
    def test_regular_array(self):
        array = [0, 1, 0, 2, 3, 0, 4, 5, 0]
        self.assertEqual(zero_counting(array), 4)

    def test_no_zeros(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(zero_counting(array), 0)

    def test_all_zeros(self):
        array = [0, 0, 0, 0, 0]
        self.assertEqual(zero_counting(array), 5)

    def test_empty_array(self):
        array = []
        self.assertEqual(zero_counting(array), 0)

    def test_single_zero(self):
        array = [0]
        self.assertEqual(zero_counting(array), 1)

    def test_single_non_zero(self):
        array = [1]
        self.assertEqual(zero_counting(array), 0)


if __name__ == "__main__":
    unittest.main()
