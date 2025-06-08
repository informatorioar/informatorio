"""Modulo dedicado a la resolucion de los ejercicios de la etapa 2 del curso de Python del Informatorio."""

# Ejercicio 1: Lista de números al revés
# Consigna: Pedir al usuario 5 números y almacenarlos en una lista. Luego mostrar la lista en orden inverso.


def lista_numeros_inversa():
    """Pide 5 números al usuario y los muestra en orden inverso."""
    numeros: list[int] = []
    for i in range(5):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)
    print("Lista de números en orden inverso:", numeros[::-1])


# Ejercicio 2: Promedio de notas
# Consigna: Pedir al usuario que ingrese las notas de una materia (hasta que escriba fin) y luego mostrar el promedio.


def promedio_notas():
    """Pide notas al usuario hasta que ingrese 'fin' y muestra el promedio."""
    notas: list[float] = []
    while True:
        entrada = input("Ingrese una nota (o 'fin' para terminar): ")
        if entrada.lower() == "fin":
            break
        try:
            nota = float(entrada)
            notas.append(nota)
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número o 'fin'.")

    if notas:
        promedio = sum(notas) / len(notas)
        print(f"El promedio de las notas es: {promedio:.2f}")
    else:
        print("No se ingresaron notas.")


# Ejercicio 3: Palabras sin repetir
# Consigna: Pedir al usuario una lista de palabras separadas por espacio y mostrar cuántas palabras distintas hay.


def contar_palabras_unicas():
    """Cuenta la cantidad de palabras únicas ingresadas por el usuario."""
    words_input = input("Ingrese una lista de palabras separadas por espacio: ")
    unique_words = set(words_input.split())
    print(f"Cantidad de palabras distintas: {len(unique_words)}")


# Ejercicio 4: Diccionario de edades
# Consigna: Pedir al usuario nombres y edades y mostrar quién es el mayor.


def encontrar_persona_mayor():
    """Almacena nombres y edades en un diccionario y muestra la persona de mayor edad."""
    personas: dict[str, str | int] = {}
    for i in range(5):
        nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
        try:
            edad = int(input(f"Ingrese la edad de {nombre}: "))
            personas[nombre] = edad
        except ValueError:
            print("Edad inválida. Debe ingresar un número.")
            return

    if personas:
        persona_mayor = max(personas.items(), key=lambda x: x[1])
        print(
            f"La persona de mayor edad es {persona_mayor[0]} con {persona_mayor[1]} años."
        )
    else:
        print("No se ingresaron datos.")


# Ejercicio 5: Contador de letras
# Consigna: Pedir al usuario una frase y contar cuántas veces aparece cada letra (ignorando espacios).


def contar_letras():
    """Cuenta la frecuencia de cada letra en una frase ingresada por el usuario."""
    phrase = input("Ingrese una frase: ")
    letter_count: dict[str, int] = {}

    for char in phrase.lower():
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1

    print("Frecuencia de cada letra:")
    for letter, count in sorted(letter_count.items()):
        print(f"'{letter}': {count}")


# Ejercicio 6: Máximo y mínimo
# Consigna: Pedir al usuario que ingrese números hasta que escriba fin. Luego mostrar el número mayor y el menor.


def encontrar_max_min():
    """Solicita números al usuario hasta que ingrese 'fin' y muestra el máximo y mínimo."""
    numbers: list[float] = []
    while True:
        entrada = input("Ingrese un número (o 'fin' para terminar): ")
        if entrada.lower() == "fin":
            break
        try:
            number = float(entrada)
            numbers.append(number)
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número o 'fin'.")

    if numbers:
        maximum = max(numbers)
        minimum = min(numbers)
        print(f"El número mayor es: {maximum}")
        print(f"El número menor es: {minimum}")
    else:
        print("No se ingresaron números.")


# Ejercicio 7: Eliminar duplicados
# Consigna: Pedir una lista de números al usuario (separados por coma) y mostrarla sin elementos repetidos.


def eliminar_duplicados():
    """Elimina números duplicados de una lista ingresada por el usuario."""
    entrada = input("Ingrese números separados por coma: ")
    try:
        # Convert string input to list of numbers
        numeros = [float(num.strip()) for num in entrada.split(",")]
        # Convert to set to remove duplicates and back to list
        numeros_unicos = list(set(numeros))
        print("Lista sin duplicados:", numeros_unicos)
    except ValueError:
        print("Entrada inválida. Ingrese números separados por coma.")


# Ejercicio 8: Posiciones de un número
# Consigna: Pedir al usuario una lista de números y un número a buscar. Mostrar en qué posiciones aparece ese número en la lista.


def encontrar_posiciones():
    """Encuentra y muestra las posiciones donde aparece un número específico en una lista."""
    entrada = input("Ingrese números separados por coma: ")
    try:
        numeros = [float(num.strip()) for num in entrada.split(",")]
        numero_buscar = float(input("Ingrese el número a buscar: "))

        posiciones = [i for i, num in enumerate(numeros) if num == numero_buscar]

        if posiciones:
            print(f"El número {numero_buscar} aparece en las posiciones: {posiciones}")
        else:
            print(f"El número {numero_buscar} no se encuentra en la lista.")
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar números válidos.")


# Ejercicio 9: Ordenar palabras
# Consigna: Pedir una lista de palabras y mostrarlas ordenadas alfabéticamente y por longitud (dos listas diferentes).


def ordenar_palabras():
    """Ordena una lista de palabras alfabéticamente y por longitud."""
    entrada = input("Ingrese palabras separadas por espacio: ")
    palabras = entrada.split()

    if not palabras:
        print("No se ingresaron palabras.")
        return

    # Sort alphabetically
    orden_alfabetico = sorted(palabras)
    # Sort by length
    orden_longitud = sorted(palabras, key=len)

    print("Palabras ordenadas alfabéticamente:", orden_alfabetico)
    print("Palabras ordenadas por longitud:", orden_longitud)


# Ejercicio 10: Inventario simple
# Consigna: Crear un diccionario que contenga nombres de productos como claves y cantidades como valores.
# Luego permitir al usuario actualizar existencias o agregar nuevos productos, hasta que escriba salir.


def gestionar_inventario():
    """Gestiona un inventario simple permitiendo agregar productos y actualizar existencias."""
    inventario: dict[str, int] = {}

    while True:
        print("\n1. Agregar/Actualizar producto")
        print("2. Ver inventario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = input("Ingrese el nombre del producto: ").strip()
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                inventario[producto] = cantidad
                print(f"Producto '{producto}' actualizado con {cantidad} unidades.")
            except ValueError:
                print("Cantidad inválida. Debe ingresar un número entero.")

        elif opcion == "2":
            if inventario:
                print("\nInventario actual:")
                for producto, cantidad in inventario.items():
                    print(f"{producto}: {cantidad}")
            else:
                print("El inventario está vacío.")

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
