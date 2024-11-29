import random
import copy

def mostrar_matriz(matriz:list) -> None:
    """
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
    """
    matriz = []

    for i in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]

    return matriz

def ocultar_datos_copia(matriz:list, caracter:any, criterio:str) -> None:
    """
    """
    # matriz_copia = matriz.copy()
    matriz_copia = copy.deepcopy(matriz)
    cantidad = 81
    porcentaje = None
    ocultos = None
    posiciones = []

    if criterio.lower() == "facil":
        porcentaje = 20

    elif criterio.lower() == "intermedio":
        porcentaje = 40

    elif criterio.lower() == "dificil":
        porcentaje = 60

    else:
        print("Acción inválida")

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
    """
    bandera = False
    for i in range(len(lista)):
        if lista[i] == numero:
            bandera = True
            break

    return bandera

def resolver_sudoku(matriz: list) -> bool:
    """
    Resuelve el Sudoku utilizando el método de backtracking.
    Devuelve True si se encuentra una solución válida, False en caso contrario.
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
    Verifica si un número ya está presente en la subcuadrícula 3x3
    correspondiente a la posición [fila][columna].
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

def comprobar_matriz(matriz:list, caracter) -> bool:
    """
    """
    completado = True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == caracter:
                completado = False
                break

        if completado == False:
            break

    return completado

def jugar_sudoku(matriz_original:list, matriz_copia:list, caracter:any) -> None:
    """
    """
    salir = False
    contador_errores = 0

    while True:
        # Mostrar la matriz al usuario
        print("\nMatriz actual:")

        for i in range(len(matriz_copia)):
            for j in range(len(matriz_copia[i])):
                if matriz_copia[i][j] == "-":
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
                        if numero_ingresar == matriz_original[i][j]:
                            print(f"Número {numero_ingresar} correcto")
                            matriz_copia[i][j] = numero_ingresar
                        
                        else:
                            print("ERROR, número incorrecto.")
                            contador_errores += 1


                else:
                    if comprobar_matriz(matriz_copia, caracter) == True:
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
        # Pedir al usuario que ingrese una posición
                


print("Inicializando matriz")
matriz = inicializar_matriz(9, 9, 0)
print("Matriz inicializada")

print()
print()
print()

print("Resolviendo sudoku")
resolver_sudoku(matriz)
mostrar_matriz(matriz)
print("Sudoku resuelto")

print()
print()
print()

dificultad = input("[1] Fácil\n[2] Intermedio\n[3] Difícil\nIngrese la dificultad en la que desea jugar: ")
matriz_copia = ocultar_datos_copia(matriz, "-", dificultad)
print()

jugar_sudoku(matriz, matriz_copia, "-")