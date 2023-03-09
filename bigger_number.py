# Ejercicio 4

number = 1
numbers_list = []
while number != 0:
    number = int(input("Número: "))
    numbers_list.append(number)

numbers_list.sort(reverse=True)
print(f"Mayor número ingresado: {numbers_list[0]}")