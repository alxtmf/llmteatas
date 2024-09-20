# Написать функцию, которая возвращает количество цифр в целом числе, получаемом в
# качестве аргумента.

import unittest

def count_digit(n):
    count = 0
    while n!= 0:
        n //= 10
        count += 1
    return count

class TestCount(unittest.TestCase):
    def test_count(self):
        def count_digit(n):
            count = 0
            while n!= 0:
                n //= 10
                count += 1
            return count

        self.assertEqual(count_digit(123), 3)
        self.assertEqual(count_digit(456), 3)
        self.assertEqual(count_digit(123456), 6)
        self.assertEqual(count_digit(123456), 6)

if __name__ == '__main__':
    unittest.main()
