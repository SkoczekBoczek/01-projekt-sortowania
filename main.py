import sys
sys.setrecursionlimit(50000)

import os
import json
import pandas as pd
from time_measurement import TimeMeasure
from sorting_algorithms import insertionSort, shellSort, selectionSort, heapSort, quickSortLeft, quickSortRandom

typesOfSort = ["random", "sorted", "reversed", "constant", "a-shaped"]
sizes = [2, 4, 8, 16, 32, 64, 100, 128, 256, 512, 1024, 2048, 4096, 5000, 8192, 10000, 16384, 32768]

algorithms = {
    "Insertion Sort": insertionSort,
    "Shell Sort": shellSort,
    "Selection Sort": selectionSort,
    "Heap Sort": heapSort,
    "Quick Sort Left": quickSortLeft,
    "Quick Sort Random": quickSortRandom
}

inputFolder = "generated_data"
data = []

for size in sizes:
    row = {"length": size}
    for type in typesOfSort:
        filename = os.path.join(inputFolder, f"data_{type}_{size}.json") 
        with open(filename, "r") as f:
            dataArray = json.load(f)
        # print(f"\n Przed sortowaniem ({type}, rozmiar {size}): {dataArray}")
        for name, algorithm in algorithms.items():
            timeRes = TimeMeasure(algorithm, dataArray)
            columnName = f"{name} - {type}"
            row[columnName] = format(timeRes, ".10f")
            print(f"\n Rozmiar: {size}, {name} - {type}, Czas: {timeRes:.10f} s")
            # print(f"Po sortowaniu: {dataCopy}")
    data.append(row)

df = pd.DataFrame(data)
print(df)
df.to_csv('sorting_results.csv', index=False)