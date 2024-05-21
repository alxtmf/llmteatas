def merge_strings(str1, str2):
    length = min(len(str1), len(str2))
    result = ''
    for i in range(length):
        if i % 2 == 0:
            result += str1[i]
        else:
            result += str2[i]
    # Если первая строка длиннее второй, добавляем оставшиеся символы с четными индексами из первой строки
    if len(str1) > len(str2):
        result += str1[length::2]
    # Если вторая строка длиннее первой, добавляем нечетные символы из второй строки
    elif len(str2) > len(str1):
        result += str2[length::2]
    return result


# Юнит-тест
def test_merge_strings():
    # Тест с разной длиной строк
    result1 = merge_strings('abcdef', '12345')
    print(result1)  # Добавленная строка для анализа
    assert result1 == 'a2c4ef'

    # Тест с одинаковой длиной строк
    assert merge_strings('abcde', '12345') == 'a2c4e'
    # Тест на пустые строки
    assert merge_strings('', '') == ''

    print("Тест пройден")


# Запуск теста
test_merge_strings()
