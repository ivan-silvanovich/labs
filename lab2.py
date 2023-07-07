import random
import time

swaps = 0
compares = 0


# Два опорных элемента. Крайние не брать
def quick_sort(arr: list) -> list:
    global swaps, compares

    if not arr or len(arr) == 1:
        return arr

    # mid = random.choice(arr)
    # mid_list = [mid] * arr.count(mid)
    # more_list = [i for i in arr if i > mid]
    # less_list = [i for i in arr if i < mid]

    a, b = sorted([arr[len(arr) // 2], arr[len(arr) // 2 - 1]])
    more_list = []
    less_list = []
    mid_list = []

    for i in arr:
        if i <= a:
            compares += 1
            swaps += 1
            less_list.append(i)
        elif i >= b:
            compares += 2
            swaps += 1
            more_list.append(i)
        else:
            compares += 2
            swaps += 1
            mid_list.append(i)

    return quick_sort(less_list) + quick_sort(mid_list) + quick_sort(more_list)


def insertion_sort(arr: list):
    global swaps, compares

    arr.insert(0, -200)

    for i in range(len(arr)):
        x = arr[i]
        j = i

        while j > 1 and arr[j - 1] > x:
            arr[j] = arr[j - 1]
            j -= 1

            compares += 2
            swaps += 1

        arr[j] = x
        compares += 1
        swaps += 1

    return result[1:]


def selection_sort(arr: list):
    global swaps, compares

    for index, _ in enumerate(arr):
        value = arr[index:].index(min(arr[index:])) + index
        arr[index], arr[value] = arr[value], arr[index]

        swaps += 2
        compares += len(arr[index:])

    return arr


def cocktail_sort(arr: list):
    global swaps, compares

    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                is_sorted = False
                swaps += 1

            compares += 1

    return arr


def heapify(arr: list, n: int, i: int):
    global swaps, compares

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    compares += 2

    if r < n and arr[largest] < arr[r]:
        largest = r

    compares += 2

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

        swaps += 1

    compares += 1


def heap_sort(arr: list):
    global swaps, compares

    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

        swaps += 1

    return arr


n = abs(int(input('Enter an amount of array\'s elements: ')))
a = -123
b = 891
# arr = [10 - i for i in range(n)]
arr = [random.randint(a, b) for i in range(n)]
for func in (quick_sort, insertion_sort, selection_sort, cocktail_sort, heap_sort, sorted):
    begin = time.time()
    result = func(arr.copy())

    print(func.__name__)
    print(f"arr: {arr}")
    print(f"result: {result}")
    print(f"time: {time.time() - begin}")
    print(f"Amount of swaps: {swaps}")
    print(f"Amount of compares: {compares}")
    print()

    swaps = 0
    compares = 0
