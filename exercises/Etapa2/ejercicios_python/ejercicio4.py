"""4. Sumar elementos de una lista Consigna: Crear una función que reciba una lista de números y devuelva la suma total. Luego usar input() para pedirle números al usuario hasta que escriba fin."""

type Number = int | float


def sumar_lista(numeros: list[Number]) -> Number:
    """Suma los elementos de una lista de números."""
    # return sum(numeros) # Utilizando un bucle for para sumar los elementos
    total: int | float = 0
    for numero in numeros:
        total += numero  # total = total + numero
    return total


def main():
    """Función principal para interactuar con el usuario."""
    numeros: list[Number] = []
    while True:
        entrada = input("Ingrese un número (o 'fin' para terminar): ")
        if entrada.lower() == "fin":
            break
        try:
            numero = float(entrada)  # Convertir la entrada a un número
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")

    total = sumar_lista(numeros)
    print(f"La suma total de los números ingresados es: {total}")


if __name__ == "__main__":
    main()
