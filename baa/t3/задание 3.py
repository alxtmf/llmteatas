def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

arr = input("Сортировка методом Шелла. Введите элементы массива:").split()
arr = [int(num) for num in arr]

print("Исходный массив:", arr)

shell_sort(arr)

print("Отсортированный массив:", arr)
import time
time.sleep(5)