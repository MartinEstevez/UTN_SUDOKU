import random

def inicializar_matriz(filas:int, columnas:int, valor:any) -> list:
    """
    """
    matriz = []
    for i in range(filas):
        fila = [valor] * columnas
        matriz += [fila]

    return matriz

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

def crear_sudoku_aleatorio(matriz:list, cantidad:int) -> None:
    """
    """
    for i in range(cantidad):
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        valor = random.randint(1, 9)

        while (verificar_numero_fila(matriz, valor, fila) == True) or (verificar_numero_columna(matriz, valor, columna) == True) or (verificar_numero_subcuadricula(matriz, valor, fila, columna) == True):
            valor = random.randint(1, 9)

        matriz[fila][columna] = valor


def crear_sudoku(matriz:list, cantidad:int) -> None:
    """
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                numeros = list(range(1, 10))

            for numero in numeros:
                if (not verificar_numero_fila(matriz, numero, i)) and (not verificar_numero_columna(matriz, numero, j)) and (not verificar_numero_subcuadricula(matriz, numero, i, j)):
                    matriz[i][j] = numero

                if crear_sudoku(matriz):
                    return True

                matriz[i][j] = 0

            return False


# def verificar_numero(matriz:list, numero:int) -> bool:
#     """
#     """
#     repetido = False
#     for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             if matriz[i][j] == numero:
#                 repetido = True
#                 break
#         if repetido == True:
#             break
    
#     return repetido

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


sudoku = inicializar_matriz(9, 9, " ")
crear_sudoku_aleatorio(sudoku, 45)
mostrar_matriz(sudoku)