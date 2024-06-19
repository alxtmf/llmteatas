# "Написать функцию, которая возвращает 1, если одномерный массив, полученный
# функцией в качестве аргумента, является упорядоченным по возрастанию."

import unittest
def func(arr):

    if len(arr) <= 1:
        return 1

    f=0
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            f = 1
        else:
            f = 0
            break
    return f


class TestFunc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(func([-1, 3, 7, 8, 10]), 1)
        self.assertEqual(func([3, 0, 2, 7, 4]), 0)
        self.assertEqual(func([2, 4, 3, 6, 8]), 0)
        self.assertEqual(func([]), 1)
        self.assertEqual(func([5]), 1)


if __name__ == '__main__':
    unittest.main()


