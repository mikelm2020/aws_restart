kilometer = float(input("Kilómetros recorridos: "))
fuel = float(input("Litros de combustible gastados: "))

if fuel > 0 and kilometer > 0:
    print(f"El consumo por kilómetro es de {kilometer/fuel}")
else:
    print("Imposible calcular el consumo!!!")