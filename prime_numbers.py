# Este script esta basasdo en la Criba de Erastótenes


# Genera la lista de candidatos a partir de los números naturales del 2 al número dado,
# en este caso al 250


def list_generator(number):
    list_numbers = [number for number in range(2, number + 1)]
    return list_numbers


# Genera la lista de números primos


def primes(number):
    list_primes = list_generator(number)
    counter = 0
    while list_primes[counter] ** 2 <= number:
        for candidate in list_primes:
            if candidate != list_primes[counter]:
                if candidate % list_primes[counter] == 0:
                    list_primes.remove(candidate)
        counter += 1
    return list_primes


# Convierte la lista de primos en cadena


def string_convert(data_list):
    return ", ".join(str(number) for number in data_list)


# Genera el archivo de texto a partir de la cadena pasada


def file_generator(data):
    with open("results.txt", mode="w") as file:
        file.write(data)


if __name__ == "__main__":
    file_generator(string_convert(primes(250)))
