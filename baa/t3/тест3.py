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

arr = [12, 13, 11, 45, 67, 23, 46]

print("Исходный массив:", arr)

shell_sort(arr)

print("Отсортированный массив:", arr)
if __name__ == "__main__":
    if arr == sorted(arr):
     print("Тест пройден")
    else:
     print("Тест не пройден")