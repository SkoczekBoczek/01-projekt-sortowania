import random

# Insertion sort
def insertionSort(array):
    arr = array.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Shell sort
def shellSort(array):
    n = len(array)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j = j - interval
            array[j] = temp
        interval = interval // 2
    return array

# Selection sort
def selectionSort(array):
    arr = array.copy()
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        (arr[i], arr[minIndex]) = (arr[minIndex], arr[i])
    return arr

# Heap sort
def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[l] > array[largest]:
        largest = l
    if r < n and array[r] > array[largest]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def heapSort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)
    return array

# Quick sort left
def quickSortLeft(arr):
    arr_copy = arr.copy()
    _quickSortLeft(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy 

def _quickSortLeft(arr, low, high):
    if low < high:
        pivot_index = partitionLeft(arr, low, high)
        _quickSortLeft(arr, low, pivot_index - 1)
        _quickSortLeft(arr, pivot_index + 1, high)

def partitionLeft(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

# Quick sort random
def quickSortRandom(arr):
    arr_copy = arr.copy()
    _quickSortRandom(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy

def _quickSortRandom(arr, low, high):
    if low < high:
        pivot_index = partitionRandom(arr, low, high)
        _quickSortRandom(arr, low, pivot_index - 1)
        _quickSortRandom(arr, pivot_index + 1, high)

def partitionRandom(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j