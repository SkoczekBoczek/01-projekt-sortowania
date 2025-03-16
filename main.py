import sys
sys.setrecursionlimit(50000)

import os
import json
import pandas as pd
from time_measurement import TimeMeasure
from sorting_algorithms import insertionSort, shellSort, selectionSort, heapSort, quickSortLeft, quickSortRandom

typesOfSort = ["random", "sorted", "reversed", "constant", "ashaped"]
sizes = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]

algorithms = {
    "Insertion Sort": insertionSort,
    "Shell Sort": shellSort,
    "Selection Sort": selectionSort,
    "Heap Sort": heapSort,
    "Quick Sort Left": quickSortLeft,
    "Quick Sort Random": quickSortRandom
}

inputFolder = "generated_data"
resultFolder = "sorting_data"

if not os.path.exists(resultFolder):
    os.mkdir(resultFolder)

def main():
    print("1. Wyświetl dane przed i po sortowaniu")
    print("2. Przeprowadź test algorytmów")
    mode = int(input("Twój wybór: "))

    if mode == 1:
        print("\nWybierz algorytm sortowania!")
        for i, name in enumerate(algorithms.keys(), 1):
            print(f"{i}: {name}")

        chooseAlgorithm = int(input("Twój wybór: "))-1
        print(list(algorithms.keys())[chooseAlgorithm])
        chosenAlgorithm = list(algorithms.values())[chooseAlgorithm]
        
        print("\nWybierz typ danych")
        for i, name in enumerate(typesOfSort, 1):
            print(f"{i}: {name}")
        chooseType = int(input("Twój wybór: "))-1
        print(typesOfSort[chooseType])
        chosenType = typesOfSort[chooseType]

        while True:
            print(f"\nWprowadź rozmiar danych: {sizes}")
            enterSize = int(input("Wybrany rozmiar: "))
            if enterSize in sizes:
                break
            else:
                print("❌ Wprowadzono nieprawidłowe dane ❌")

        filename = os.path.join(inputFolder, f"data_{chosenType}_{enterSize}.json")
        with open(filename, "r") as f:
            dataArray = json.load(f)

        print(f"\nPrzed sortowaniem: {dataArray}")
        sortedDataArray = chosenAlgorithm(dataArray)
        print(f"Po sortowaniu: {sortedDataArray}")

    elif(mode == 2):
        data = []
        for size in sizes:
            for type in typesOfSort:
                filename = os.path.join(inputFolder, f"data_{type}_{size}.json") 
                with open(filename, "r") as f:
                    dataArray = json.load(f)
                for name, algorithm in algorithms.items():
                    timeRes = TimeMeasure(algorithm, dataArray)
                    algorithmType = f"{name}-{type}"
                    data.append([algorithmType, size, format(timeRes, ".10f")])
                    print(f"\n Rozmiar: {size}, {name} - {type}, Czas: {timeRes:.10f} s")

        groupedData = {}
        for row in data:
            algorithmType = row[0]
            type = algorithmType.split("-")[1]
            if type not in groupedData:
                groupedData[type] = []
            groupedData[type].append(row)

        for type, rows in groupedData.items():
            df = pd.DataFrame(rows, columns=["Algorithm","Size","Time"])
            print(df)
            df.to_csv(f"{resultFolder}/results_{type}.csv", index=False)
    else:
        print("x")

main()
