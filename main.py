import pygame
from Biblioteca_funciones import *


pygame.init() #inicializo pygame 
pygame.mixer.init() #inicializo musica

pantalla_actual = "Inicio"

pantalla = inicializar_caracteristicas_pantalla(1534, 801, "Super Sudoku","Segundo_parcial\icono_ventanita.jpg")

actualizar_pantalla = True #botones titilando
ultimo_etado_del_mouse = None #botones titilando


ruta_imagen_inicio = "Segundo_parcial/pantalla_inicio.png"
ruta_imagen_seleccion_niveles = "Segundo_parcial/pantalla_eleccion_nivel.png"

pygame.mixer.music.load("Segundo_parcial/musica_inicio.mp3") #sonido largo de fondo
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1, start=0.0)

corriendo = True
while corriendo == True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False #cierro juego
        
        if pantalla_actual == "Inicio":
            mostrar_pantalla_inicio(pantalla, ruta_imagen_inicio)
            actualizar_pantalla = False
            pygame.mixer.music.stop() #SACAR ESTO

            if evento.type == pygame.MOUSEMOTION: #movimiento del mouse
                x, y = pygame.mouse.get_pos()
                # accion = obtener_accion(x, y)
                mouse_actual = (x,y)
                if mouse_actual != ultimo_etado_del_mouse:
                    actualizar_pantalla = True
                    ultimo_etado_del_mouse = mouse_actual
                else: 
                    actualizar_pantalla = False
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                accion = obtener_accion(x, y)
            
                if accion == "Jugar":
                    pygame.mixer.music.stop() #poner musica nueva SACAR ESTO
                    pantalla_actual = "Seleccion niveles"
                    actualizar_pantalla = True
                elif accion == "Puntajes":
                    pass #muestra puntajes
                elif accion == "Salir": 
                    corriendo = False
            
            if actualizar_pantalla: 
                mostrar_pantalla_inicio(pantalla, ruta_imagen_inicio)
                actualizar_pantalla = False

        elif pantalla_actual == "Seleccion niveles":
            mostrar_pantalla_niveles(pantalla, ruta_imagen_seleccion_niveles)
            

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                nivel = obtener_accion_niveles(x, y)
                if nivel == "Facil":
                    pantalla_actual = "Facil"
                    cargar_fondo_y_musica_segun_nivel(pantalla, "Facil")
                    colores_nivel_actual = asignar_colores_sudoku_segun_nivel("Facil")
                    actualizar_pantalla = True
                    pygame.mixer.music.stop() #SACAR ESTO
                    
                elif nivel == "Medio":
                    pantalla_actual = "Medio"
                    cargar_fondo_y_musica_segun_nivel(pantalla, "Medio")
                    colores_nivel_actual =  asignar_colores_sudoku_segun_nivel("Medio")
                    actualizar_pantalla = True
                    pygame.mixer.music.stop() #SACAR ESTO

                elif nivel == "Dificil":
                    pantalla_actual = "Dificil"
                    cargar_fondo_y_musica_segun_nivel(pantalla, "Dificil")
                    colores_nivel_actual = asignar_colores_sudoku_segun_nivel("Dificil")
                    actualizar_pantalla = True
                    pygame.mixer.music.stop() #SACAR ESTO

                mostrar_sudoku(pantalla, colores_nivel_actual["lineas"][0], colores_nivel_actual["lineas"][1], colores_nivel_actual["lineas"][2], colores_nivel_actual["fondo"])
                # mostrar_numeros_dentro_sudoku(pantalla, funciondeltablero)

        # elif pantalla_actual == "Medio":   
        #     pass
        # elif pantalla_actual == "Dificil":
        #     pass
    
    
    
    
    
    
    # pantalla.fill((60,15,0)) #color de fondo 

    pygame.display.flip() #actualiza pmatlla 
pygame.mixer.music.stop()
pygame.quit() #sale de pygame







# corriendo = True
# while corriendo == True:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             corriendo = False #cierro juego
        
#         mostrar_pantalla_inicio(pantalla, ruta_imagen_inicio)
        
#         if evento.type == pygame.MOUSEBUTTONDOWN:
#             x, y = pygame.mouse.get_pos()
#             accion = obtener_accion(x, y)
            
#             if accion == "Jugar":
#                 pygame.mixer.music.stop()
#                 #poner musica nueva 
#             elif accion == "Puntajes":
#                 pass #muestra puntajes
#             elif accion == "Salir": 
#                 corriendo = False
























































