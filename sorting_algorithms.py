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
    arr = array.copy()
    n = len(arr)
    gaps = []
    k = 0
    while True:
        gap = 4**k + 3 * 2**(k-1) + 1 if k > 0 else 1
        if gap > n:
            break
        gaps.append(gap)
        k += 1
    
    gaps.reverse()
    
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    
    return arr

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

# Quick sort left - podział Hoare’a ✅  (❌ Lomuto Partition ❌)
def quickSortLeft(array):
    arr = array.copy()
    _quickSortLeft(arr, 0, len(arr) - 1)
    return arr 

def _quickSortLeft(array, low, high):
    if low < high: # Jeśli jest więcej niż 1 element, wykonujemy sortowanie
        pivotIndex = partitionLeft(array, low, high) # Dzielimy tablicę
        _quickSortLeft(array, low, pivotIndex - 1) # Sortujemy lewą część
        _quickSortLeft(array, pivotIndex + 1, high) # Sortujemy prawą część

def partitionLeft(array, low, high):
    pivot = array[low]
    i = low + 1
    j = high
    while True:
        while i <= j and array[i] <= pivot:
            i += 1 # Szukamy pierwszego elementu większego niż pivot po lewej stronie
        while i <= j and array[j] > pivot:
            j -= 1 # Szukamy pierwszego elementu mniejszego niż pivot po prawej stronie
        if i >= j:
            break
        array[i], array[j] = array[j], array[i] # Wieksze na prawo mniejsze na lewo
    array[low], array[j] = array[j], array[low] # Pivocik jest przesuwany 
    return j

# Quick sort random - podział Hoare’a ✅  (❌ Lomuto Partition ❌)
def quickSortRandom(array):
    arr = array.copy()
    _quickSortRandom(arr, 0, len(arr) - 1)
    return arr

def _quickSortRandom(array, low, high):
    if low < high:
        pivotIndex = partitionRandom(array, low, high)
        _quickSortRandom(array, low, pivotIndex - 1)
        _quickSortRandom(array, pivotIndex + 1, high)

def partitionRandom(array, low, high):
    pivotIndex = random.randint(low, high)
    array[low], array[pivotIndex] = array[pivotIndex], array[low] # pivocik leci na poczatek 
    pivot = array[low] # Ustawiamy pivocika jako pierwszy element
    i = low + 1
    j = high
    while True:
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i >= j:
            break
        array[i], array[j] = array[j], array[i]
    array[low], array[j] = array[j], array[low]
    return j 