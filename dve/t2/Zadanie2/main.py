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

    return arr
def test_shell_sort():
    test_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = shell_sort(test_array.copy())
    if sorted_array == sorted(test_array):
        print("тест пройден")
    else:
        print("тест не пройден")
test_shell_sort()
