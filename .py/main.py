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
texto_ingresado = ""
activo = True

# 4) En el menú principal o al finalizar la partida, el jugador debe poder ingresar su nombre a través de una caja de texto en la pantalla del juego (NO mediante la terminal).

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

                matriz_copia = ocultar_datos_copia(matriz, 0, porcentaje)
                    


    if pantalla_actual in ["Facil", "Medio", "Dificil"]:
        pantalla.fill((255, 255, 255))  # Limpia la pantalla antes de redibujar
        
        # Fondo y música según el nivel
        cargar_fondo_y_musica_segun_nivel(pantalla, pantalla_actual)

        # Dibujar el botón de menú y el temporizador
        boton_menu = mostrar_boton_menu(pantalla)
        texto, rect = iniciar_contador(contador_inicio, fuente, (1400, 50), (0, 0, 0))
        pantalla.blit(texto, rect)

        # Dibujar el tablero y los números
        matriz_celdas = mostrar_tablero(pantalla, celda_seleccionada)
        mostrar_numeros_dentro_sudoku(pantalla, matriz_copia, matriz)

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Verificar si se presionó el botón de menú
                if boton_menu.collidepoint((x, y)):
                    pantalla_actual = "Inicio"
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("musica_inicio.mp3")  # Cargar música inicial
                    pygame.mixer.music.set_volume(0.4)
                    pygame.mixer.music.play(loops=-1, start=0.0)
                else:
                    # Seleccionar una celda si se hace clic en el tablero
                    nueva_celda = seleccionar_celda(x, y, matriz_celdas)
                    if nueva_celda != celda_seleccionada:
                        celda_seleccionada = nueva_celda
                        print(f"Celda seleccionada: {celda_seleccionada}")
        
            elif evento.type == pygame.KEYDOWN and celda_seleccionada:
                i, j = celda_seleccionada  # Desempaquetar la celda seleccionada

                # Solo permitir la modificación si la celda está vacía
                if matriz_copia[i][j] == 0:  
                    if pygame.K_1 <= evento.key <= pygame.K_9:  # Teclas del 1 al 9
                        numero = evento.key - pygame.K_0  # Convertir tecla a número

                        # Actualizar la matriz editable con el número ingresado
                        matriz_copia[i][j] = numero
                        print(f"Número ingresado: {numero} en celda ({i}, {j})")
                        
                        # Verificar si el Sudoku está completo y bien resuelto
                        if comprobar_matriz(matriz, matriz_copia):
                            print("¡Felicidades! El Sudoku está completo y bien resuelto.")

                # Verificar si se presiona la tecla BACKSPACE y si el número es editable (diferente de la matriz original)
                elif evento.key == pygame.K_BACKSPACE and matriz_copia[i][j] != matriz[i][j]:
                    matriz_copia[i][j] = 0  # Borrar el número de la celda
                    print(f"Se borró el número en la celda ({i}, {j})")
                    
                else:
                    print(f"La celda ({i}, {j}) es fija y no se puede modificar.")
            
    #
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