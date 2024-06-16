# "Написать функцию, которая вычисляет произведение элементов массива,
# расположенных между элементами с номерами i и j. Массив и номера i и j передаются в
# функцию в качестве аргументов."

def product_between_indices(array, i, j):
    if i > j:
        i, j = j, i

    product = 1
    for i in range(i + 1, j):
        product *= array[i]

    return product

def print_test_result(array, i, j, expected):
    result = product_between_indices(array, i, j)
    print(f"Массив: {array}")
    print(f"Индексы: i={i}, j={j}")
    print(f"Ожидаемый результат: {expected}")
    print(f"Фактический результат: {result}")
    print("Результат теста:", "Прошел" if result == expected else "Не прошел")
    print()

array1 = [2, 3, 4, 5, 6]
i1, j1 = 1, 4
expected1 = 20
print_test_result(array1, i1, j1, expected1)

array2 = [1, 2, 3, 4, 5, 6]
i2, j2 = 5, 1
expected2 = 60
print_test_result(array2, i2, j2, expected2)

array3 = [7, 8, 9, 10, 11, 12]
i3, j3 = 0, 3
expected3 = 72
print_test_result(array3, i3, j3, expected3)