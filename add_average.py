# Tercer ejercicio

numbers = []
for i in range(6):
    numbers.append(int(input("Número: ")))

negatives = [number for number in numbers if number < 0]
positives = [number for number in numbers if number > 0]

if len(negatives) == 0:
    print("Sumatoría de los negativos: 0")
else:
    print(f"Sumatoría de los negativos: {sum(negatives)}")

if len(positives) == 0:
    print("Promedio de los positivos: 0")
else:
    print(f"Promedio de los positivos: {sum(positives) / len(positives)}")
