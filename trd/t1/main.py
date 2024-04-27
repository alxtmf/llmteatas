import unittest

def shift_string(text, shift_amount):

    non_space_chars = [c for c in text if c != ' ']  
    shift_amount %= len(non_space_chars)

    rotated_chars = non_space_chars[-shift_amount:] + non_space_chars[:-shift_amount]

    result = ""
    i = 0
    for char in text:
        if char != ' ':
            result += rotated_chars[i]
            i += 1
        else:
            result += ' '
    return result

class TestShiftString(unittest.TestCase):

    def test_shift_string(self):
        self.assertEqual(shift_string("Я люблю программировать", 2), "т ьЯлюб люпрограммирова")

if __name__ == '__main__':
    text = input("Введите текст: ").strip()
    shift_amount = int(input("Введите число сдвига: "))

    shifted_string = shift_string(text, shift_amount)
    print("Итог:", shifted_string)

    unittest.main()
