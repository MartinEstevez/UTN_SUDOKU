import random
lista = []

def mostrar_lista(lista:list) -> None:
    """
    """
    for i in range(len(lista)):
        if len(lista) != i+1:
            print(lista[i], end=" - ")

        else:
            print(lista[i])

import random

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

def carga_secuencial(matriz:list) -> None:
    """
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(1, 9)


def ocultar_datos(matriz:list, caracter:any, cantidad:int) -> None:
    """
    """
    for _ in range(cantidad):
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        matriz[fila][columna] = caracter

import random

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
            if matriz[i][j] == 0:  # Celda vacía encontrada
                solucion_encontrada = False  # Aún no hay solución completa

                # Probar números del 1 al 9
                for numero in lista_random:
                    if (not verificar_numero_fila(matriz, numero, i)
                        and not verificar_numero_columna(matriz, numero, j)
                        and not verificar_numero_subcuadricula(matriz, numero, i, j)):

                        # Asignar número
                        matriz[i][j] = numero

                        # Llamar recursivamente
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


print("Inicializando matriz")
matriz = inicializar_matriz(9, 9, 0)
print("Matriz inicializada")
mostrar_matriz(matriz)


print()
print()
print()

print("Resolviendo sudoku")
resolver_sudoku(matriz)
mostrar_matriz(matriz)
print("Sudoku resuelto")