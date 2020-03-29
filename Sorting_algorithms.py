import time
import csv
import random


def test_sort(v):
    if sorted(v) == v:
        return "List is sorted."
    else:
        return "List is not sorted."


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def count_sort(arr, max_val):
    m = max_val + 1
    count = [0] * m

    for i in arr:
        count[i] += 1
    j = 0

    for i in range(m):

        for k in range(count[i]):
            arr[j] = i
            j += 1


# functie countSort implementata ca subrutina a Radix Sortului
def countSort(arr, pas):
    length_ar = len(arr)
    v = [0] * length_ar
    b = [0] * length_ar

    for i in range(length_ar):
        v[(arr[i] // pas) % 10] = v[(arr[i] // pas) % 10] + 1

    for i in range(length_ar):
        v[i] = v[i] + v[i - 1]

    for i in range(length_ar - 1, -1, -1):
        v[(arr[i]) // pas % 10] = v[(arr[i]) // pas % 10] - 1
        b[v[(arr[i]) // pas % 10]] = arr[i]

    for i in range(length_ar):
        arr[i] = b[i]


def radix_sort(arr):
    max1 = max(arr)
    pas = 1

    while max1 // pas > 0:
        countSort(arr, pas)
        pas = pas * 10


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):

            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):

    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


j = 0
with open('tests.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    Arr = []

    for line in csv_reader:
        j = j + 1
        print("TEST ", end='')
        print(j)
        length = line[0]
        assert isinstance(length, object)
        length = int(length)
        Max = line[1]
        assert isinstance(Max, object)
        Max = int(Max)
        print("Lungimea sirului este: ", end='')
        print(length)
        print("Valoarea maxima posibila este:", end='')
        print(Max)
        print("Sirul generat este: ", end='')
        Arr = []

        for i in range(length):
            Arr.insert(i, random.randint(1, Max))  # se genereaza un sir random de lungime length
        print('\n')
        Cop = Arr  # creez o copie pentru sir
        m_val = max(Arr)  # valoarea maxima a sirului generat
        aux = len(Arr)

        print("QUICK SORT")
        start = time.time()
        quick_sort(Arr, 0, aux - 1)
        end = time.time()
        print(test_sort(Arr))
        print("Timp de rulare: ", end='')
        print(end - start)
        Arr = Cop

        print("BUBBLE SORT")
        start = time.time()
        bubble_sort(Arr)
        end = time.time()
        print(test_sort(Arr))
        print("Timp de rulare: ", end='')
        print(end - start)
        Arr = Cop

        print("MERGE SORT")
        start = time.time()
        merge_sort(Arr)
        end = time.time()
        print(test_sort(Arr))
        print("Timp de rulare: ", end='')
        print(end - start)
        Arr = Cop

        print("COUNT SORT")
        start = time.time()
        count_sort(Arr, m_val)
        end = time.time()
        print(test_sort(Arr))
        print("Timp de rulare: ", end='')
        print(end - start)
        Arr = Cop

        print("RADIX SORT")
        start = time.time()
        radix_sort(Arr)
        end = time.time()
        print(test_sort(Arr))
        print("Timp de rulare: ", end='')
        print(end - start)
        Arr = Cop

        print("PYTHON SORT")
        start = time.time()
        Arr.sort()
        end = time.time()
        print(test_sort(Arr))
        print("Timp de rulare: ", end='')
        print(end - start)
        Arr = Cop
        print('\n')
