# "Дана строка. Заменить все символы идущие подряд на 1 символ. К
# примеру, строка «ааа ррр о вввв» преобразуется в строку «а р о в»."

import unittest

def func(s):
    if not s:
        return ""

    result = s[0]
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
            result+=s[i]

    return result


class TestFunc(unittest.TestCase):

    def test_func(self):
        self.assertEqual(func("ааа ррр о вввв"), "а р о в")
        self.assertEqual(func("а   р о в"), "а р о в")
        self.assertEqual(func("fff grgr ggggttt"),"f grgr gt")

if __name__ == '__main__':
    unittest.main()


