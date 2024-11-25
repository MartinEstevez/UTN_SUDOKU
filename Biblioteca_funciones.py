import pygame 

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
    pygame.display.flip()

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
    if nivel == "Facil":
        fondo = pygame.image.load("Segundo_parcial/pantalla_nivel_facil.png")
        pygame.mixer.music.load("Segundo_parcial/musica_nivel_facil.mp3") #sonido largo de fondo

    elif nivel == "Medio": 
        fondo = pygame.image.load("Segundo_parcial/pantalla_nivel_medio.png")
        pygame.mixer.music.load("Segundo_parcial/musica_nivel_medio.mp3")

    elif nivel == "Dificil":
        fondo = pygame.image.load("Segundo_parcial/pantalla_nivel_dificil.png")
        pygame.mixer.music.load("Segundo_parcial/musica_nivel_dificil.mp3")

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

