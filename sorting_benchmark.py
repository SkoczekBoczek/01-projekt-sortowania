import time
import random
import pandas as pd

# Insertion sort
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key
    return array

# Shell sort
def shellSort(array):
    n = len(array)
    interval = n//2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while  j >= interval and array[j - interval] > temp: 
                array[j] = array[j-interval]
                j = j-interval
            array[j] = temp
        interval = interval//2
    return array

# Selection sort
def selectionSort(array):
    n = len(array)
    for i in range(n):
        minIndex = i 
        for j in range(i+1, n):
            if(array[minIndex] > array[j]):
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    return array

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

# Quick sort
def QuickSort(array):
    return 


# ===== GENEROWANIE DANYCH =====
def aShapeArray(size):
    array = [0] * size
    for i in range(size // 2):
        array[i] = 2 * i + 1
    for i in range(size // 2, size):
        array[i] = 2 * (size - i)
    return array

def generateData(type, size):
    if(type == "random"):
        return [random.randint(0, 1000) for _ in range(size)]
    elif(type == "sorted"):
        return list(range(size))
    elif(type == "reversed"):
        return list(range(size))[::-1]
    elif(type == "constant"):
        return [69]*size
    elif(type == "a-shaped"):
        return aShapeArray(size) 
    


# ===== POMIAR CZASU SORTOWANIA =====
def TimeMeasure(sortFunction, data):
    dataCopy = data[:]
    startTime = time.time()
    sortFunction(dataCopy)
    endTime = time.time()
    timeRes = round((endTime - startTime), 10)
    return timeRes



# ===== TESTOWANIE I ZAPIS DO PLIKU =====
typesOfSort = ["random", "sorted", "reversed", "constant", "a-shaped"]
sizes = [1000, 5000, 10000]
algorithms = {
    "Insertion Sort": insertionSort,
    "Shell Sort": shellSort,
    "Selection Sort": selectionSort,
    "Heap Sort": heapSort,
}


data = []

for size in sizes:
    row = {"length": size}
    for type in typesOfSort:
        for name, algorithm in algorithms.items():
            dataArray = generateData(type, size)
            timeRes = TimeMeasure(algorithm, dataArray)
            columnName = f"{name} - {type}"
            row[columnName] = timeRes
    data.append(row)

df = pd.DataFrame(data)
print(df)
df.to_csv('sorting_results.csv', index=False)

# for name, algorithm in algorithms.items():
#     for type in typesOfSort:
#         print(f"\n🐥 Testowanie: {name}, Dane: {type}")
#         for size in sizes:
#             data = generateData(type, size)
#             dataCopy = data[:]
#             resTime, sortedData = TimeMeasure(algorithm, dataCopy)
#             print(f"\n Rozmiar: {size}, {name}: {sortedData[:10]}..., Czas: {resTime:.10f} s")