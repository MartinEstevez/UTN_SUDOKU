import random
import copy

def mostrar_matriz(matriz:list) -> None:
    """
    Imprime una matriz en formato tabular, separando los elementos con " | " 
    y las filas con líneas de guiones.

    Recibe:
        matriz (list): lista de listas que representa la matriz a mostrar.
    """
    guiones = "-" * (len(matriz[0]) + ((len(matriz[0])-1) * 3))

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if len(matriz[i]) != j+1:
                print(matriz[i][j], end=" | ")

            else:
                print(matriz[i][j])

        if len(matriz) != i+1:
            print(guiones)

def inicializar_matriz(filas:int, columnas:int, valor_inicial:any) -> list:
    """
    Crea una matriz de dimensiones especificadas, inicializando cada posición con un valor dado.

    Recibe:
        filas (int): cantidad de filas de la matriz.
        columnas (int): cantidad de columnas de la matriz.
        valor_inicial (any): valor con el que se inicializarán todas las posiciones de la matriz.

    Devuelve:
        list (list): matriz creada con las dimensiones y valores especificados.
    """
    matriz = []

    for i in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]

    return matriz

def ocultar_datos_copia(matriz:list, caracter:any, porcentaje:int) -> list:
    """
    Crea una copia de una matriz y reemplaza un porcentaje de sus elementos con un caracter especificado,
    seleccionando las posiciones de manera aleatoria.

    Recibe:
        matriz (list): lista de listas que representa la matriz original.
        caracter (any): valor que reemplazará los elementos en las posiciones seleccionadas.
        porcentaje (int): porcentaje de elementos a reemplazar en la matriz.

    Devuelve:
        matriz_copia: copia de la matriz original con los elementos reemplazados según el porcentaje.
    """
    # matriz_copia = matriz.copy()
    matriz_copia = copy.deepcopy(matriz)
    cantidad = 81
    ocultos = None
    posiciones = []

    ocultos = (cantidad * porcentaje) // 100
    
    for fila in range(9):
        for columna in range(9):
            posiciones.append([fila, columna])  # Crea una lista con todas las posiciones que puede haber

    
    for _ in range(ocultos):
        indice = random.randint(0, len(posiciones) - 1)  # Va a elegir una posición de la lista de posiciones
        posicion = posiciones.pop(indice)  # Elimina la posición para no volver a seleccionarla
        fila = posicion[0]  # Número de la fila
        columna = posicion[1]  # Número de la columna
        matriz_copia[fila][columna] = caracter

    return matriz_copia

def verificar_numero(lista:list, numero:int) -> bool:
    """
    Verifica si un número está presente en una lista.

    Recibe:
        lista (list): lista de elementos donde se buscará el número.
        numero (int): número a buscar en la lista.

    Devuelve:
        bandera (bool): True si el número está presente en la lista, False en caso contrario.
    """
    bandera = False
    for i in range(len(lista)):
        if lista[i] == numero:
            bandera = True
            break

    return bandera

def resolver_sudoku(matriz: list) -> list:
    """
    Resuelve un Sudoku utilizando el método de recursividad.
    Completa las celdas vacías de la matriz (representadas por ceros) con valores válidos.

    Recibe:
        matriz (list): lista de listas que representa la cuadrícula del Sudoku (9x9), donde las celdas vacías están representadas por ceros.

    Devuelve:
        solucion_encontrada (list): matriz del Sudoku resuelta con todas las celdas correctamente completadas.
    """
    lista_random = []
    for _ in range(9):
        numero_random = random.randint(1, 9)
        while verificar_numero(lista_random, numero_random) == True:
            numero_random = random.randint(1, 9)

        lista_random.append(numero_random)
    
    solucion_encontrada = True
    # Encuentra la primera celda vacía
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:  # Encuentra la primera celva vacía
                solucion_encontrada = False

                # Probar números del 1 al 9
                for numero in lista_random:
                    # Si el número no se repite en la fila, columna y subcuadrícula
                    if (not verificar_numero_fila(matriz, numero, i)
                        and not verificar_numero_columna(matriz, numero, j)
                        and not verificar_numero_subcuadricula(matriz, numero, i, j)):

                        # Asigna el número
                        matriz[i][j] = numero

                        # Vuelve a llamar a la función
                        if resolver_sudoku(matriz):  # Si se resuelve, marcar como solucionado
                            solucion_encontrada = True
                            break

                        # Deshacer asignación si no funciona
                        matriz[i][j] = 0

                # Si no se encontró solución, salir del bucle
                if solucion_encontrada != True:
                    break

        if solucion_encontrada != True:
            break

    return solucion_encontrada
    
def verificar_numero_columna(matriz:list, numero:int, columna:int):
    """
    Verifica si un número ya está presente en una columna de la matriz.

    Recibe:
        matriz (list): lista de listas que representa la cuadrícula del Sudoku.
        numero (int): número que se va a verificar en la columna.
        columna (int): índice de la columna donde se verificará la presencia del número.

    Devuelve:
        repetido (bool): True si el número ya está presente en la columna, False en caso contrario.
    """
    repetido = False
    for i in range(len(matriz)):
        if matriz[i][columna] == numero:
            repetido = True
            break

    return repetido

def verificar_numero_fila(matriz:list, numero:int, fila:int):
    """
    """
    repetido = False
    for i in range(len(matriz[fila])):
        if matriz[fila][i] == numero:
            repetido = True
            break

    return repetido

def verificar_numero_subcuadricula(matriz: list, numero: int, fila: int, columna: int) -> bool:
    """
    Verifica si un número ya está presente en una fila de la matriz.

    Recibe:
        matriz (list): lista de listas que representa la cuadrícula del Sudoku.
        numero (int): número que se va a verificar en la fila.
        fila (int): índice de la fila donde se verificará la presencia del número.

    Devuelve:
        repetido (bool): True si el número ya está presente en la fila, False en caso contrario.
    """
    fila_inicio = (fila // 3) * 3
    columna_inicio = (columna // 3) * 3
    repetido = False

    for i in range(fila_inicio, fila_inicio + 3):
        for j in range(columna_inicio, columna_inicio + 3):
            if matriz[i][j] == numero:
                repetido = True  # Número ya está en la subcuadrícula
                break

        if repetido == True:
            break

    return repetido

def comprobar_matriz(matriz:list, matriz_copia:list) -> bool:
    """
    Verifica si todos los elementos de la matriz están completos, es decir, si la matriz está resuelta

    Recibe:
        matriz (list): lista de listas que representa la matriz a comprobar.
        matriz_copia (list): lista de listas que representa la copia de la matriz a comparar.

    Devuelve:
        completado (bool): True si todos los elementos de la matriz están completos, False si al menos una celda contiene un valor diferente.
    """
    completado = True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz_copia[i][j] != matriz[i][j]:  # Si no coincide con la solución correcta
                completado = False
                break

        if completado == False:
            break

    return completado

def jugar_sudoku(matriz_original:list, matriz_copia:list, caracter:any) -> None:
    """
    Simula un juego de Sudoku donde el jugador intenta completar una copia de la matriz original, ingresando números en las celdas vacías. El juego termina cuando se completan todas las celdas correctamente o cuando el jugador decide salir.

    Recibe:
        matriz_original (list): matriz que representa la solución correcta del Sudoku.
        matriz_copia (list): matriz que el jugador debe completar, inicialmente contiene celdas vacías.
        caracter (any): valor que indica las celdas vacías en la matriz (por ejemplo, 0 o algún valor específico).

    El juego permite al jugador:
        - Ingresar un número en una celda vacía.
        - Verificar si el número ingresado es correcto.
        - Mostrar el estado de la matriz después de cada jugada.
        - Salir del juego si lo desea.
        - El jugador recibe puntos por respuestas correctas y se penaliza por respuestas incorrectas.
        - El juego termina cuando la matriz está completa o el jugador decide salir.
    """
    salir = False
    contador_errores = 0

    while True:
        # Mostrar la matriz al usuario
        print("\nMatriz actual:")

        for i in range(len(matriz_copia)):
            for j in range(len(matriz_copia[i])):
                # if ord(matriz_copia[i][j]) < 49 or ord(matriz_copia[i][j]) > 57:
                if matriz_copia[i][j] == caracter:
                    print()
                    mostrar_matriz(matriz_copia)
                    print(f"\nErrores: {contador_errores}")
                    numero_ingresar = int(input(f"\nPosición:\n- Fila {i + 1}\n- Columna {j + 1}\nIngrese un número (1-9, o -1 para salir, 0 para saltar): "))

                    if numero_ingresar == -1:  # Salida del juego
                        print("Gracias por jugar. ¡Hasta luego!")
                        salir = True
                        break

                    elif numero_ingresar == 0:
                        continue

                    else:
                        # while numero_ingresar != matriz_original:
                        if numero_ingresar == matriz_original[i][j]:
                            print(f"Número {numero_ingresar} correcto")
                            # puntos += 100
                            matriz_copia[i][j] = numero_ingresar
                        
                        else:
                            print("ERROR, número incorrecto.")
                            contador_errores += 1

                else:
                    if comprobar_matriz(matriz, matriz_copia) == True:
                        salir = True
                        if contador_errores == 1:
                            print(f"¡Ha completado el juego con {contador_errores} error!")
                        else:
                            print(f"¡Ha completado el juego con {contador_errores} errores!")

                        mostrar_matriz(matriz_copia)
                        break

            if salir == True:
                break

        if salir == True:
            break

matriz = inicializar_matriz(9, 9, 0)
resolver_sudoku(matriz)
mostrar_matriz(matriz)

print()

matriz_copia = ocultar_datos_copia(matriz, " ", 10)
mostrar_matriz(matriz_copia)

print()

jugar_sudoku(matriz, matriz_copia, " ")