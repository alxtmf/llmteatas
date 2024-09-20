# Даны две строки. Сформировать третью строку таким образом, чтобы
# в нее попеременно вошли четные символы первой строки и нечетные символы второй
# строки. В качестве длины третьей строки взять длину меньшей из введенных строк.

import unittest

def third_line(str1, str2):
    result = ""
    min_len = min(len(str1), len(str2))
    for i in range(min_len):
        if i % 2 == 0:
            result += str1[i]
        else:
            result += str2[i]
    return result

class TestThirdLine(unittest.TestCase):
    def test_third_line(self):
        self.assertEqual(third_line("hello", "world"), "hollo")
        self.assertEqual(third_line("abc", "defgh"), "aec")
        self.assertEqual(third_line("short", "verylongstring"), "seoyt")
        self.assertEqual(third_line("", "hello"), "")
        self.assertEqual(third_line("hello", ""), "")

    def test_input_types(self):
        with self.assertRaises(TypeError):
            third_line(123, "hello")
        with self.assertRaises(TypeError):
            third_line("hello", 123)

    def test_empty_strings(self):
        self.assertEqual(third_line("", ""), "")

if __name__ == "__main__":
    unittest.main()