import pygame
import json
from Biblioteca_funciones import *

pygame.init()

archivo_json = "/puntajes.json"

def cargar_puntajes(archivo_json):
    """
    Carga un archivo JSON con los puntajes de los jugadores.
    
        archivo_json (str): Ruta al archivo JSON.
    
    Return:
        list: Una lista de puntajes si el archivo es válido; en caso de no encontrar el archivo, una lista vacía.
    """
    try:
        with open(archivo_json, 'r') as archivo:
            return json.load(archivo)
    except Exception as e:
        print(f"Error al cargar el archivo JSON: {e}")
        return []
    
def mostrar_puntajes(pantalla, puntajes):
    """
    Muestra una lista de puntajes en terminal.

    """
    fuente = pygame.font.Font(None, 55)
    color_texto = (0, 0, 0)

    x, y = 600, 300
    espacio_vertical = 100

    for i, entrada in enumerate(puntajes):
        texto = f"{i + 1}. {entrada.get('nombre', ' ')}: {entrada.get('puntaje', )}"
        texto_renderizado = fuente.render(texto, True, color_texto)
        pantalla.blit(texto_renderizado, (x, y))
        y += espacio_vertical

puntajes = cargar_puntajes("puntajes.json")
print(puntajes)

def mostrar_pantalla_puntajes_jugadores(pantalla:pygame.Surface, ruta_imagen:str) -> None:
    
    """
    Función para mostrar la pantalla del top de puntajes.

    """

    imagen_ranking = pygame.image.load(ruta_imagen)
    imagen_ranking = pygame.transform.scale(imagen_ranking, pantalla.get_size())
    pantalla.blit(imagen_ranking, (0, 0))
    
    x_menu = 750
    y_menu = 700

    fuente_30 = pygame.font.SysFont("Arial", 40)
    texto_menu = fuente_30.render("MENU", True, "#000000")
    boton_menu = texto_menu.get_rect(center=(x_menu, y_menu))
    menu = pygame.Rect.inflate(boton_menu, 10, 10)
    pygame.draw.rect(pantalla, "#000000", menu, 3)

    pantalla.blit(texto_menu, boton_menu)

    return menu

    pygame.display.update()














