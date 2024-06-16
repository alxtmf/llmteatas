# "Дана строка. Вычислить длину строки без учета пробелов и знаков
# препинания."

def length_without_spaces_and_punctuation(s):
    clean_s = ""
    for char in s:
        if char.isalnum():
            clean_s += char
    return len(clean_s)

def print_test_result(input_string, expected_length):
    result = length_without_spaces_and_punctuation(input_string)
    print(f"Строка: '{input_string}'")
    print(f"Ожидаемая длина: {expected_length}")
    print(f"Фактическая длина: {result}")
    print("Результат теста:", "Прошел" if result == expected_length else "Не прошел")
    print()

test_string1 = "Hello, world!"
expected_length1 = 10
print_test_result(test_string1, expected_length1)

test_string2 = "Python 3.8.5"
expected_length2 = 9
print_test_result(test_string2, expected_length2)

test_string3 = " Spaces and... punctuation!!!"
expected_length3 = 20
print_test_result(test_string3, expected_length3)