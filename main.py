import sys
sys.setrecursionlimit(50000)

import os
import json
import pandas as pd
from matplotlib import pyplot as plt
from time_measurement import TimeMeasure
from sorting_algorithms import insertionSort, shellSort, selectionSort, heapSort, quickSortLeft, quickSortRandom

typesOfSort = ["random", "sorted", "reversed", "constant", "ashaped"]
sizes = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
# sizes = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

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
plotFolder = "wykresy"

# ===== TWORZENIE WYKRESÓW =====
def generate_plots():
    if not os.path.exists(plotFolder):
        os.makedirs(plotFolder)
        print(f"Utworzono folder: {plotFolder}")
        
    for type in typesOfSort:
        filepath = os.path.join(resultFolder, f"results_{type}.csv")
        df = pd.read_csv(filepath)
        for algorithm in df["Algorithm"].unique():
            algorithmData = (df[df["Algorithm"] == algorithm])
            plt.plot(algorithmData["Size"], algorithmData["Time"], marker='o', label=algorithm)

        plt.xlabel("Liczba elementów")
        plt.ylabel("Czas (s)") 
        plt.title(f"Porównanie czasów sortowania - {type}")
        plt.legend()
        plt.grid(True) #siatka

        plotFolderPath = os.path.join(plotFolder, f"wykres_{type}")
        plt.savefig(plotFolderPath)
        plt.close()
        print(f"Wykres zapisano do folderu {plotFolderPath}")

def main():
    print("1. Wyświetl dane przed i po sortowaniu")
    print("2. Przeprowadź test algorytmów")
    mode = int(input("Twój wybór: "))

    if mode == 1:
# ===== WYBÓR ALGORYTMU =====
        while True:
            print("\nWybierz algorytm sortowania!")
            for i, name in enumerate(algorithms.keys(), 1):
                print(f"{i}: {name}")
            chooseAlgorithm = int(input("Twój wybór: "))-1

            if chooseAlgorithm in range(0, len(algorithms)):
                print(list(algorithms.keys())[chooseAlgorithm])
                chosenAlgorithm = list(algorithms.values())[chooseAlgorithm]
                break
            else:
                print("❌ Taki algorytm nie istnieje ❌")

# ===== WYBÓR TYPU DANYCH =====   
        while True:
            print("\nWybierz typ danych")
            for i, name in enumerate(typesOfSort, 1):
                print(f"{i}: {name}")
            chooseType = int(input("Twój wybór: "))-1

            if chooseType in range(0, len(typesOfSort)):
                print(typesOfSort[chooseType])
                chosenType = typesOfSort[chooseType]
                break
            else:
                print("❌ Taki typ danych nie istnieje ❌")

# ===== WYBÓR ROZMIARU TABLICY =====
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

        print(f"{chosenAlgorithm} - {chosenType}")
        print(f"\nPrzed sortowaniem: {dataArray}")
        sortedDataArray = chosenAlgorithm(dataArray)
        print(f"Po sortowaniu: {sortedDataArray}")
        
# ===== TESTOWANIE I ZAPIS DO PLIKÓW =====
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

        if not os.path.exists(resultFolder):
            os.mkdir(resultFolder)

        groupedData = {}
        for row in data:
            algorithmType = row[0]
            type = algorithmType.split("-")[1]
            if type not in groupedData:
                groupedData[type] = []
            groupedData[type].append(row)

        for type, rows in groupedData.items():
            df = pd.DataFrame(rows, columns=["Algorithm","Size","Time"])
            df.to_csv(f"{resultFolder}/results_{type}.csv", index=False)

# ===== TWORZENIE WYKRESÓW =====
        print()
        generate_plots()
    else:
        print("Źle wybrałeś unlucky :( ")

main()