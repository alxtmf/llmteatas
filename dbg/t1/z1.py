# "В одномерном массиве, состоящем из N целых элементов, вычислите сумму
# модулей элементов массива, расположенных после первого элемента, равного 0"

import random
import unittest

def func(arr):
    sum=0
    for i in range(len(arr)):
        if arr[i] == 0:
           t = i
           arr2 = arr[t+1::]
           for i in range(len(arr2)):
               sum=sum+abs(arr2[i])
           break
    return sum



# a = int(input("Введите размер массива"))
# arr = [0]
# arr = arr + [random.randint(-10, 10) for i in range(a-1)]
# random.shuffle(arr)
# func(arr)

class TestFuncArray(unittest.TestCase):

    def test_add(self):
        self.assertEqual(func([1, 2, 4, 0, -3, 7]), 10)
        self.assertEqual(func([-3, 0, 4, 0, 6, -5]), 15)
        self.assertEqual(func([1, -3, 0, 4, 6, -3]), 13)


if __name__ == '__main__':
    unittest.main()

