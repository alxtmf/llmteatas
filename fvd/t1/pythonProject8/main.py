def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
def test_bubble_sort():
    arr = ['banana', 'apple', 'orange', 'grape']
    bubble_sort(arr)
    assert is_sorted(arr), "Тест не пройден"
    print("Тест пройден")
test_bubble_sort()
