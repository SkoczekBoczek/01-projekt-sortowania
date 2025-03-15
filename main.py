import os
import json
import pandas as pd
from time_measurement import TimeMeasure
from sorting_algorithms import insertionSort, shellSort, selectionSort, heapSort, quickSort

typesOfSort = ["random", "sorted", "reversed", "constant", "a-shaped"]
sizes = [1000, 5000, 10000, 50000]
algorithms = {
    "Insertion Sort": insertionSort,
    "Shell Sort": shellSort,
    "Selection Sort": selectionSort,
    "Heap Sort": heapSort,
    "Quick Sort": quickSort
}

inputFolder = "generated_data"
data=[]

for size in sizes:
    for type in typesOfSort:
        row = {"Length": size}
        filename = os.path.join(inputFolder, f"data_{type}_{size}.json")
        with open(filename, "r") as f:
            dataArray = json.load(f)
        for name, algorithm in algorithms.items():
            timeRes = TimeMeasure(algorithm ,dataArray)
            columnName = f"{name} - {type}"
            row[columnName] = timeRes
            print(f"\n Rozmiar: {size}, {name} - {type}, Czas: {timeRes} s")
    data.append(row)

df = pd.DataFrame(data)
print(df) 
df.to_csv('sorting_results.csv', index=False)