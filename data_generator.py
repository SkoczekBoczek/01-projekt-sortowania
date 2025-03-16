import os
import random
import json

def aShapeArray(size):
    array = [0] * size
    for i in range(size // 2):
        array[i] = 2 * i + 1
    for i in range(size // 2, size):
        array[i] = 2 * (size - i)
    return array

def generateData(type, size):
    if type == "random":
        return [random.randint(0, 1000) for _ in range(size)]
    elif type == "sorted":
        return list(range(size))
    elif type == "reversed":
        return list(range(size))[::-1]
    elif type == "constant":
        return [69] * size
    elif type == "ashaped":
        return aShapeArray(size)


typesOfSort = ["random", "sorted", "reversed", "constant", "ashaped"]
sizes = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]

folder = "generated_data"
if not os.path.exists(folder):
   os.makedirs(folder)
   print(f"Utworzono folder: {folder}")

for size in sizes:
    for type in typesOfSort:
        dataArray = generateData(type, size)
        filename = os.path.join(folder, f"data_{type}_{size}.json")
        with open(filename, "w") as f:
            json.dump(dataArray, f)
        print(f"Wygenerowano i zapisano dane do pliku: {filename}")