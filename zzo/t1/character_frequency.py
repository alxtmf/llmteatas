"""Дана строка. Определить, какой символ чаще всего встречается."""

from collections import Counter
import unittest


def character_frequency(s):
    return Counter(s).most_common(1)[0][0] if Counter(s) else None


class TestCharacterFrequency(unittest.TestCase):
    def test_regular_string(self):
        self.assertEqual(character_frequency("abracadabra"), "a")

    def test_empty_string(self):
        self.assertIsNone(character_frequency(""))

    def test_single_character(self):
        self.assertEqual(character_frequency("a"), "a")

    def test_tie_characters(self):
        self.assertEqual(character_frequency("ab"), "a")

    def test_all_unique_characters(self):
        self.assertEqual(character_frequency("abcdef"), "a")


if __name__ == "__main__":
    unittest.main()
