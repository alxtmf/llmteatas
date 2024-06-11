import random

def func(x):
    sum=0
    arr = [0]
    arr = arr + [random.randint(-10, 10) for i in range(x-1)]
    random.shuffle(arr)
    print(arr)
    for i in range(len(arr)):
        if arr[i] == 0:
           t = i
           arr2 = arr[t+1::]
           for i in range(len(arr2)):
               sum=sum+abs(arr2[i])
           break
    print(sum)

a = int(input("Введите размер массива"))
func(a)


