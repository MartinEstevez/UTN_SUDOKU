import pygame
from sudoku_original import *

#CARACTERISTICAS PANTALLA
def inicializar_caracteristicas_pantalla(ancho:int, largo:int, titulo_juego:str, ruta_icono:str) -> pygame.Surface: #que devuelve? surface?
    """"
    Esta función permite permite inicializar las caracteristicas de la pantalla general del juego.

    Recibe:
        ancho (int): ancho de la pantalla.
        largo (int): largo de la pantalla.
        titulo_juego (str): título del juego.
        ruta_icono (str): la ruta relativa del ícono del juego.

    Retorna:
        pygame.Surface: superficie de la pantalla.
    """
    # info_pantalla  = pygame.display.Info()
    # ancho = info_pantalla.current_w
    # alto = info_pantalla.current_h
    
    pantalla = pygame.display.set_mode((ancho, largo))
    pygame.display.set_caption(titulo_juego)
    imagen_ventana = pygame.image.load(ruta_icono) #ruta relativa
    pygame.display.set_icon(imagen_ventana)
    
    return pantalla

#PANTALLA INICIO
def dibujar_boton(pantalla:pygame.Surface, x:int, y:int, ancho:int, alto:int, texto:str, color_boton:str, color_texto_boton:str) -> None:
    """
    Esta función permite dibujar los botones de las pantallas.

    Recibe:
        pantalla (pygame.Surface): superficie en donde se van a dibujar los botones.
        x (int): eje horizontal de la pantalla.
        y (int): eje vertical de la pantalla.
        ancho (int): ancho del botón.
        alto (int): alto del botón.
        texto (str): texto del botón.
        color_boton (str): color del botón.
        color_texto_boton (str): color del texto que va adentro del botón.
    """
    pygame.draw.rect(pantalla, color_boton,(x, y, ancho, alto))
    
    fuente_letras = pygame.font.SysFont("Arial", 80)
    texto = fuente_letras.render(texto, True, color_texto_boton)
    
    texto_rectangulo = texto.get_rect(center=(x + ancho // 2, y + alto // 2))
    
    pantalla.blit(texto, texto_rectangulo)

def mostrar_pantalla_inicio(pantalla:pygame.Surface, ruta_imagen:str) -> None:
    """
    Esta función permite mostrar la pantalla de inicio con los botones incluidos.

    Recibe:
        pantalla (pygame.Surface): superficie en donde va a estar la pantalla.
        ruta_imagen (str): ruta relativa de la imagen de la pantalla de inicio.
    """
    imagen_inicio = pygame.image.load(ruta_imagen)
    imagen_inicio = pygame.transform.scale(imagen_inicio, pantalla.get_size())
    pantalla.blit(imagen_inicio, (0, 0))

    ancho_del_boton = 500
    alto_del_boton = 150
    espacios_entre_los_botones = 80
    posicion_horizontal_boton = 918 #x
    posicion_vertical_incial_boton = 95 #y

    dibujar_boton(pantalla, posicion_horizontal_boton, posicion_vertical_incial_boton, ancho_del_boton, alto_del_boton, "Jugar", (188, 211, 242), (128, 164, 238))
    dibujar_boton(pantalla, posicion_horizontal_boton, posicion_vertical_incial_boton + alto_del_boton + espacios_entre_los_botones, ancho_del_boton, alto_del_boton, "Puntajes", (188, 211, 242), (128, 164, 238))
    dibujar_boton(pantalla, posicion_horizontal_boton, posicion_vertical_incial_boton + 2*(alto_del_boton + espacios_entre_los_botones), ancho_del_boton, alto_del_boton, "Salir", (188, 211, 242), (128, 164, 238))

def obtener_accion(x:int, y:int) -> str:
    """
    Esta función permite obtener la acción del click del mouse en la pantalla inicial.

    Recibe:
        x (int): eje horizontal de la pantalla.
        y (int): eje vertical de la pantalla.

    Retorna:
        str: acción a realizar según click del mouse.
    """
    accion = None
    ancho_del_boton = 500
    alto_del_boton = 150
    espacios_entre_los_botones = 80
    posicion_horizontal_boton = 918 #x
    posicion_vertical_incial_boton = 95 #y

    if posicion_horizontal_boton <= x <= posicion_horizontal_boton + ancho_del_boton:
        if posicion_vertical_incial_boton <= y <=  posicion_vertical_incial_boton + alto_del_boton:
            accion = "Jugar"
        elif posicion_vertical_incial_boton + alto_del_boton + espacios_entre_los_botones <= y <= posicion_vertical_incial_boton + 2 *(alto_del_boton + espacios_entre_los_botones):
            accion = "Puntajes"
        elif posicion_vertical_incial_boton + 2 * (alto_del_boton + espacios_entre_los_botones) <= y <= posicion_vertical_incial_boton + 3 *(alto_del_boton + espacios_entre_los_botones):
            accion = "Salir"
    return accion

#PANTALLA SELECCION DE NIVELES
def mostrar_pantalla_niveles(pantalla:pygame.Surface, ruta_imagen:str) -> None:
    """
    Esta función permite mostrar la pantalla de niveles con los botones incluidos.

    Recibe:
        pantalla (pygame.Surface): superficie en donde va a estar la pantalla.
        ruta_imagen (str): ruta relativa de la imagen de la pantalla de niveles.
    """
    imagen_seleccion_niveles = pygame.image.load(ruta_imagen)
    imagen_seleccion_niveles = pygame.transform.scale(imagen_seleccion_niveles, pantalla.get_size())
    pantalla.blit(imagen_seleccion_niveles, (0, 0))

    ancho_del_boton = 400
    alto_del_boton = 150
    espacios_entre_los_botones = 50
    posicion_horizontal_boton = 115 #x
    posicion_vertical_incial_boton = 535 #y

    dibujar_boton(pantalla, posicion_horizontal_boton, posicion_vertical_incial_boton, ancho_del_boton, alto_del_boton, "Facil", (56, 92, 106), (128, 164, 238))
    dibujar_boton(pantalla, posicion_horizontal_boton + ancho_del_boton + espacios_entre_los_botones, posicion_vertical_incial_boton, ancho_del_boton, alto_del_boton, "Medio", (56, 92, 106), (128, 164, 238))
    dibujar_boton(pantalla, posicion_horizontal_boton + 2*(ancho_del_boton + espacios_entre_los_botones), posicion_vertical_incial_boton , ancho_del_boton, alto_del_boton, "Dificil", (56, 92, 106), (128, 164, 238))

def obtener_accion_niveles(x:int, y:int) -> str:
    """
    Esta función permite obtener la acción del click del mouse en la pantalla de niveles.

    Recibe:
        x (int): eje horizontal de la pantalla.
        y (int): eje vertical de la pantalla.

    Retorna:
        str: acción a realizar según click del mouse.
    """
    accion = None
    ancho_del_boton = 400
    alto_del_boton = 150
    espacios_entre_los_botones = 50
    posicion_horizontal_boton = 115 #x
    posicion_vertical_incial_boton = 535 #y

    if posicion_horizontal_boton <= x <= posicion_horizontal_boton + ancho_del_boton:
        if posicion_vertical_incial_boton <= y <=  posicion_vertical_incial_boton + alto_del_boton:
            accion = "Facil"
    
    elif posicion_horizontal_boton + ancho_del_boton + espacios_entre_los_botones <= x <= posicion_horizontal_boton + 2 * ancho_del_boton + espacios_entre_los_botones:
        if posicion_vertical_incial_boton <= y <=  posicion_vertical_incial_boton + alto_del_boton:
            accion = "Medio"
    
    elif posicion_horizontal_boton + 2 * (ancho_del_boton + espacios_entre_los_botones) <= x <= posicion_horizontal_boton + 3 *ancho_del_boton + 2 * espacios_entre_los_botones:
        if posicion_vertical_incial_boton <= y <=  posicion_vertical_incial_boton + alto_del_boton:
            accion = "Dificil"
    return accion

#NIVELES
def cargar_fondo_y_musica_segun_nivel(pantalla:pygame.Surface, nivel:str) -> pygame.Surface: #devuelve surface?
    """
    Esta función permite cargar el fondo y la pantalla según el nivel elegido.

    Recibe:
        pantalla (pygame.Surface): superficie donde va a estar la pantalla.
        nivel (str): nivel elegido.

    Retorna:
        pygame.Surface: superficie en donde va a estar la pantalla.
    """
    pygame.mixer.music.stop() 
    if nivel == "Facil":
        fondo = pygame.image.load("img/pantalla_nivel_facil.png")
        pygame.mixer.music.load("music/musica_nivel_facil.mp3") #sonido largo de fondo

    elif nivel == "Medio": 
        fondo = pygame.image.load("img/pantalla_nivel_medio.png")
        pygame.mixer.music.load("music/musica_nivel_medio.mp3")

    elif nivel == "Dificil":
        fondo = pygame.image.load("img/pantalla_nivel_dificil.png")
        pygame.mixer.music.load("music/musica_nivel_dificil.mp3")

        #FIJATE ESTO

    #ajuste de fondo al tamaño de la pantalla
    fondo = pygame.transform.scale(fondo, pantalla.get_size())
    pantalla.blit(fondo, (0, 0))

    pygame.mixer.music.set_volume(0.4) #volumen de pantalla
    pygame.mixer.music.play(-1) #se repite la cancion

    return fondo


def mostrar_sudoku(pantalla:pygame.Surface, cantidad_rojo:int, cantidad_verde:int, cantidad_azul:int, color_fondo:tuple) -> None:
    """
    Esta función dibuja el sudoku.

    Recibe:
        pantalla (pygame.Surface): superficie en donde se va a mostrar el sudoku.
        cantidad_rojo (int): cantidad de rojo de las lineas.
        cantidad_verde (int): cantidad de verde de las lineas. 
        cantidad_azul (int): cantidad de azul de las lineas.
        color_fondo (tuple): color de fondo de las celdas del sudoku
    """
    tamanio_celda = 87
    alto_sudoku = 10 * tamanio_celda
    ancho_sudoku = 9 * tamanio_celda

    color_lineas_sudoku = (cantidad_rojo, cantidad_verde, cantidad_azul) #lineas
    color_lineas_separadoras_sudoku = (cantidad_rojo, cantidad_verde, cantidad_azul)

    #fondo
    for fila in range(9):
        for columna in range(9):
            color_fondo_celda = color_fondo
            pygame.draw.rect(pantalla, color_fondo_celda, pygame.Rect(columna * tamanio_celda, fila * tamanio_celda, tamanio_celda, tamanio_celda))

    #lineas horizontales
    for fila in range(10):
        if fila % 3 == 0:
            grosor = 5
            color = color_lineas_separadoras_sudoku
        else: 
            grosor = 1
            color = color_lineas_sudoku

        pygame.draw.line(pantalla, color, (0, fila * tamanio_celda), (ancho_sudoku, fila * tamanio_celda), grosor)
    
    #lineas verticales
    for columna in range(10): 
        if columna % 3 == 0:
            grosor = 5
            color = color_lineas_separadoras_sudoku
        else: 
            grosor = 1
            color = color_lineas_sudoku

        pygame.draw.line(pantalla, color, (columna * tamanio_celda, 0), (columna * tamanio_celda, alto_sudoku), grosor)

    #borde
    pygame.draw.rect(pantalla, color_lineas_sudoku, pygame.Rect(0, 0, ancho_sudoku, alto_sudoku), 3)

def mostrar_numeros_dentro_sudoku(pantalla:pygame.Surface, tablero:list) -> None:
    """
    Esta función permite mostrar los numeros dentro del sudoku.

    Recibe:
        pantalla (pygame.Surface): superficie en donde se van a poner esos números.
        tablero (list): lista de números.
    """
    tamanio_celda = 60
    fuente_numeros = pygame.font.SysFont("Arial", 32) #tamaño fuente

    for i in range(9):
        for j in range(9): 
            y = (i * tamanio_celda) + tamanio_celda // 4
            x = (j * tamanio_celda) + tamanio_celda // 4 #centra el numero  
            
            if tablero[i][j] != 0: #si no hay numero lo dibuja
                texto = fuente_numeros.render(str(tablero[i][j]), True, (0, 0, 0)) #color numeros
                pantalla.blit(texto, (x,y))

def asignar_colores_sudoku_segun_nivel(nivel:str) -> dict:
    """"
    Esta función permite asignar diferentes colores al tablero según el nivel seleccionado.

    Recibe:
        nivel (str): nivel elegido.

    Retorna:
        dict: dicccionario de colores según el nivel elegido.
    """
    colores = {} #diccionario

    if nivel == "Facil": 
        colores = {
            "lineas": (188, 211, 242), 
            "lineas_separadoras":(188, 211, 242),
            "fondo": (128, 164, 238) 
        }
    elif nivel == "Medio":
        colores = {
            "lineas": (128, 164, 238),
            "lineas_separadoras":(0, 0, 128),
            "fondo": (230, 225, 196)
        }
    elif nivel == "Dificil": 
        colores = {
            "lineas": (56, 92, 106),
            "lineas_separadoras":(128, 0, 0),
            "fondo": (188, 211, 242)
        }
    return colores

def iniciar_contador(contador_inicio:int, fuente:str, posicion:int,color_texto) -> None:
    """
    Calcula el tiempo transcurrido desde el inicio del contador y genera el texto del countdown.

        contador_inicio (int): Tiempo de inicio del contador en milisegundos.
        fuente (pygame.font.Font): Fuente a usar para renderizar el texto.
        posicion: Posición (x, y)
        color_texto: Color del texto en formato RGB.
    """
    tiempo_transcurrido = (pygame.time.get_ticks() - contador_inicio) / 1000
    horas = int(tiempo_transcurrido // 3600)
    minutos = int((tiempo_transcurrido % 3600) // 60)
    segundos = int(tiempo_transcurrido % 60)

    tiempo_texto = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    texto = fuente.render(tiempo_texto, True, color_texto)
    rect = texto.get_rect(center=posicion)

    return texto, rect

def mostrar_pantalla_puntaje(pantalla:pygame.Surface, ruta_imagen:str) -> None:
    
    """
    Función para mostrar la pantalla de puntaje.

    """

    imagen_puntajes = pygame.image.load(ruta_imagen) #busca la ruta de la imagen para el fondo
    imagen_puntajes = pygame.transform.scale(imagen_puntajes, pantalla.get_size())
    pantalla.blit(imagen_puntajes, (0, 0))
    
    fuente_texto_menu = pygame.font.SysFont("Arial", 30)
    fuente_texto_puntaje = pygame.font.SysFont("Arial", 25)

    texto_menu = fuente_texto_menu.render("VOLVER", True, "#000000")
    boton_menu = texto_menu.get_rect(center=(400, 500))
    borde_boton = pygame.Rect.inflate(boton_menu, 10, 10)
    pygame.draw.rect(pantalla, "#000000", borde_boton, 5)

    texto_tiempo = fuente_texto_puntaje.render(f"TIEMPO: ", True, (0, 0, 0))
    texto_errores = fuente_texto_puntaje.render(f"ERRORES: ", True, (0, 0, 0))
    texto_dificultad = fuente_texto_puntaje.render(f"DIFICULTAD: ", True, (0, 0, 0))
    texto_puntaje = fuente_texto_puntaje.render(f"PUNTAJE OBTENIDO: ", True, (0, 0, 0))

    pantalla.blit(texto_menu, boton_menu)
    pantalla.blit(texto_tiempo)
    pantalla.blit(texto_errores)
    pantalla.blit(texto_dificultad)
    pantalla.blit(texto_puntaje)

def obtener_accion_boton_volver(coordenada_x:int, coordenada_y:int) -> str:
    """
    Esta función detecta si se hizo click en el botón volver.

    Args:
        x (int): _description_
        y (int): _description_

    Returns:
        str: _description_
    """
    accion = None
    boton_x = 950
    boton_y = 570
    alto_boton = 400
    ancho_boton = 150

    if boton_x <= coordenada_x <= boton_x + ancho_boton and boton_y <= coordenada_y <= boton_y + alto_boton:
        accion = "Volver"
    return accion 

def mostrar_boton_menu(pantalla:pygame.Surface) -> None: 

    """ 
    Esta funcion dibuja un boton de menu en pantalla para poder volver al menu principal.

    Retorna: El area del boton

    """

    x_menu = 1400
    y_menu = 700

    fuente_30 = pygame.font.SysFont("Arial", 40)
    texto_menu = fuente_30.render("MENU", True, "#000000")
    # boton_menu = texto_menu.get_rect(center=(x_menu, y_menu)
    boton_menu = texto_menu.get_rect()
    boton_menu.x = x_menu
    boton_menu.y = y_menu
    pygame.draw.rect(pantalla, "#000000", boton_menu, 3)

    pantalla.blit(texto_menu, boton_menu)

    return boton_menu

def mostrar_tablero(pantalla:pygame.Surface, celda_seleccionada:tuple) -> list:

    tamanio_celda = 87
    alto_celda = 85
    ancho_celda = 85
    color_fondo = (255, 255, 255)
    color_fondo_celda = (0, 0, 0)
    linea_gruesa_grosor = 7
    linea_gruesa_color = (0,0,0)
    color_celda = (0, 0, 0)

    ancho_rect = 765
    alto_rect = 800

    matriz_celdas = inicializar_matriz(9, 9, None)

    # for fila in range(9):
    #     for columna in range(9):
    pygame.draw.rect(pantalla, color_fondo_celda, pygame.Rect(0, 0, ancho_rect, alto_rect))

    for fila in range(9):
        for columna in range(9):
            x = columna * tamanio_celda
            y = fila * tamanio_celda
            if celda_seleccionada and celda_seleccionada == (fila, columna):
                color_fondo_celda = (255, 255, 0)  # Amarillo para la celda seleccionada
            else:
                color_fondo_celda = color_fondo  # Blanco para las celdas no seleccionadas

            # Dibujar la celda
            celda = pygame.draw.rect(pantalla, color_fondo_celda, pygame.Rect(x, y, alto_celda, ancho_celda))
            matriz_celdas[fila][columna] = celda
            
    
    #lineas divisorias subcuadricula
    for i in range(10):
        if i % 3 == 0: #horizontal
            pygame.draw.line(pantalla, linea_gruesa_color, (0, i * tamanio_celda), (9* tamanio_celda, i* tamanio_celda),linea_gruesa_grosor)
        else:
            pygame.draw.line(pantalla, color_celda, (0, i * tamanio_celda), (9* tamanio_celda, i * tamanio_celda), 1)

        if i % 3 == 0: #verticales
            pygame.draw.line(pantalla, linea_gruesa_color, (i * tamanio_celda, 0), (i* tamanio_celda, 9* tamanio_celda),linea_gruesa_grosor)
        else:
            pygame.draw.line(pantalla, color_celda, (i * tamanio_celda, 0), (i* tamanio_celda , 9 * tamanio_celda), 1)

    


    return matriz_celdas

def seleccionar_celda(x: int, y: int, matriz_celdas: list) -> tuple:
    """
    Detecta la celda seleccionada con base en las coordenadas (x, y) del clic.

    Args:
        x (int): Coordenada horizontal del clic.
        y (int): Coordenada vertical del clic.
        matriz_celdas (list): Matriz de rectángulos representando las celdas del tablero.

    Returns:
        tuple: Índices (fila, columna) de la celda seleccionada. Retorna None si no se selecciona ninguna celda.
    """


    for fila in range(len(matriz_celdas)):
        for columna in range(len(matriz_celdas[fila])):
            if matriz_celdas[fila][columna].collidepoint(x, y):  # Detectar clic dentro del rectángulo
                celda_seleccionada = (fila, columna)
    
    return celda_seleccionada

def resaltar_celda(pantalla:pygame.Surface, fila:int, columna:int, matriz_celdas):
    celda = matriz_celdas[fila][columna]  # Obtener la celda correspondiente
    pygame.draw.rect(pantalla, (255, 255, 0), celda)

def mostrar_numeros_dentro_sudoku(pantalla: pygame.Surface, matriz_copia: list, matriz:list) -> None:
    """
    Renderiza los números en el tablero y los pinta de verde si son válidos,
    o rojo si son incorrectos.
    """
    tamanio_celda = 87
    fuente_numeros = pygame.font.SysFont("Arial", 32)  # Tamaño de fuente

    for i in range(9):
        for j in range(9):
            if matriz_copia[i][j] != 0:  # Si la celda no está vacía
                numero = matriz_copia[i][j]

                # Determinar el color del número según su validez
                if numero != matriz[i][j]:
                    color = (255, 0, 0)  # Verde para válidos
                else:
                    color = (0, 0, 0)  # Negro

                # Posicionar el número en el centro de la celda
                x = j * tamanio_celda + tamanio_celda // 2
                y = i * tamanio_celda + tamanio_celda // 2
                texto = fuente_numeros.render(str(numero), True, color)
                rect_celda = pygame.Rect(j * tamanio_celda, i * tamanio_celda, tamanio_celda, tamanio_celda)
                texto_rect = texto.get_rect(center=rect_celda.center)
                pantalla.blit(texto, texto_rect)


    # # Validar fila
    # if numero in matriz[fila]:
    #     return True

    # # Validar columna
    # for i in range(9):
    #     if matriz[i][columna] == numero:
    #         return True

    # # Validar subcuadrícula 3x3
    # inicio_fila = (fila // 3) * 3
    # inicio_columna = (columna // 3) * 3
    # for i in range(inicio_fila, inicio_fila + 3):
    #     for j in range(inicio_columna, inicio_columna + 3):
    #         if matriz[i][j] == numero:
    #             return False

    # # Si pasa todas las validaciones
    # return True

def comprobar_juego_correcto(matriz: list) -> bool:
    """
    Comprueba si el tablero está completamente resuelto y correcto según las reglas del Sudoku.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            num = matriz[i][j]
            if num == 0:  # Verifica que no haya celdas vacías
                return False
            if (verificar_numero_fila(matriz, num, i) or
                verificar_numero_columna(matriz, num, j) or
                verificar_numero_subcuadricula(matriz, num, i, j)):
                return False
    return True
# def finalizar_juego(matriz:list, caracter, numero:int) -> bool:
#     """
#     """
#     completado = True
#     for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             if (matriz[i][j] == caracter) or numero != matriz[i][j] :
#                 completado = False
#                 break

#         if completado == False:
#             break


def finalizar_juego():
    """
    Imprime un mensaje al finalizar el juego.
    """
    print("Juego finalizado")

    pygame.display.flip()