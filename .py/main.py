import pygame
from Biblioteca_funciones import *
from puntajes import *
from sudoku_original import *

pygame.init() #inicializo pygame 
pygame.mixer.init() #inicializo musica

#Pantalllas 
pantalla = inicializar_caracteristicas_pantalla(1534, 801, "Super Sudoku","img/icono_ventanita.jpg")

#Rutas
ruta_imagen_inicio = "img/pantalla_inicio.png"
ruta_imagen_seleccion_niveles = "img/pantalla_eleccion_nivel.png"
ruta_imagen_puntajes = "img/puntajes.png"

#Musica 
pygame.mixer.music.load("music/musica_inicio.mp3") #sonido largo de fondo
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1, start=0.0)

#Timer

contador_inicio = pygame.time.get_ticks()  # Tiempo inicial para el contador
fuente = pygame.font.SysFont("Arial", 30)  # Fuente para el contador

pantalla_actual = "Inicio"
corriendo = True
celda_seleccionada = None

while corriendo == True:
    
    if pantalla_actual == "Inicio":
        
        pantalla.fill((255,255,255))
        
        mostrar_pantalla_inicio(pantalla, ruta_imagen_inicio)
        
        pygame.mixer.music.stop()
        
        for evento in pygame.event.get():
            #cerrar pantalla
            if evento.type == pygame.QUIT:
                corriendo = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                accion = obtener_accion(x, y)

                if accion == "Jugar":
                    pygame.mixer.music.stop() #poner musica nueva SACAR ESTO
                    matriz = inicializar_matriz(9, 9, 0)
                    resolver_sudoku(matriz)
                    pantalla_actual = "Seleccion niveles"
            
                elif accion == "Puntajes":
                    pantalla_actual = "Puntajes"
                        
                elif accion == "Salir": 
                    corriendo = False
    

    elif pantalla_actual == "Seleccion niveles":

        pantalla.fill((255,255,255))

        mostrar_pantalla_niveles(pantalla, ruta_imagen_seleccion_niveles)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                nivel = obtener_accion_niveles(x, y)

                if nivel == "Facil":
                    porcentaje = 20

                    pantalla_actual = "Facil"
                    cargar_fondo_y_musica_segun_nivel(pantalla, "Facil")

                elif nivel == "Medio":
                    porcentaje = 40
                    pantalla_actual = "Medio"
                    cargar_fondo_y_musica_segun_nivel(pantalla, "Medio")
                    
                elif nivel == "Dificil":
                    porcentaje = 60
                    pantalla_actual = "Dificil"
                    cargar_fondo_y_musica_segun_nivel(pantalla, "Dificil")

                matriz_copia = ocultar_datos_copia(matriz, " ", porcentaje)
                    

    #VUELVA AL MENU
    elif pantalla_actual in ["Facil", "Medio", "Dificil"]:

        pantalla.fill((255,255,255))

        cargar_fondo_y_musica_segun_nivel(pantalla, pantalla_actual)

        boton_menu = mostrar_boton_menu(pantalla)

        texto, rect = iniciar_contador(contador_inicio, fuente, (1400, 50), (0, 0, 0))
        pantalla.blit(texto, rect)

        matriz_celdas = mostrar_tablero(pantalla, celda_seleccionada)
        
        mostrar_numeros_dentro_sudoku(pantalla, matriz_copia)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False


            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if boton_menu.collidepoint((x, y)):
                    pantalla_actual = "Inicio"
                    actualizar_pantalla = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("musica_inicio.mp3")  # sonido largo de fondo
                    pygame.mixer.music.set_volume(0.4)
                    pygame.mixer.music.play(loops=-1, start=0.0)
    
    # Verificar si se hace clic en alguna celda
                elif seleccionar_celda(x, y, matriz_celdas):
                    celda_seleccionada = seleccionar_celda(x, y, matriz_celdas)
                    print(f"Celda seleccionada: {celda_seleccionada}")
                    if celda_seleccionada:
                        fila, columna = celda_seleccionada
                        resaltar_celda(pantalla, fila, columna, matriz_celdas)

                        # CELDA SELECCIONADA = (X, Y) --> PINTAR ESA CELDA DE COLOR AMARILLO
                        nueva_celda = seleccionar_celda(x, y, matriz_celdas)                   
                    elif nueva_celda != celda_seleccionada:  # Solo cambiar si es una celda diferente
                            celda_seleccionada = nueva_celda
                    else:
                        print("No se encontor ninguna celda")
                        celda_seleccionada = None

            elif evento.type == pygame.KEYDOWN and celda_seleccionada is not None:

                if evento.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                    numero = int(pygame.key.name(evento.key))  # Convertir la tecla presionada a un número
                    fila, columna = celda_seleccionada
                    matriz[fila][columna] = numero  # Actualizar la matriz con el número ingresado
                    print(f"Ingresado número {numero} en la celda ({fila}, {columna})")
                    
                    tamaño_celda = 87

                    # Calculamos las posiciones x e y en píxeles
                    x_pos = columna * tamaño_celda  # X de la celda
                    y_pos = fila * tamaño_celda    # Y de la celda

                    # Centramos el número dentro de la celda (ajustamos un poco el valor)
                    texto_numero = fuente.render(str(numero), True, (0, 0, 0))  # Renderizar el número en negro
                    # Centrado en la celda (ajustamos para que quede en el centro exacto de la celda)
                    ancho_numero = texto_numero.get_width()
                    alto_numero = texto_numero.get_height()
                    pantalla.blit(texto_numero, (x_pos + (tamaño_celda - ancho_numero) // 2, y_pos + (tamaño_celda - alto_numero) // 2))


    elif pantalla_actual == "Puntajes":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

            mostrar_pantalla_puntajes_jugadores(pantalla, ruta_imagen_puntajes)
            mostrar_puntajes(pantalla, puntajes)

            mostrar_boton_menu(pantalla) # SEPARAR BOTONES SEGUN PANTALLA 

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                pantalla_actual = "Inicio"
                actualizar_pantalla = True

    pygame.display.flip()


pygame.mixer.music.stop()
pygame.quit()