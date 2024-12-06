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
    
    # try:
    with open(archivo_json, 'r') as archivo:
        mi_archivo = json.load(archivo) # QUEDARNOS CON UN SOLO RETURN (POR FUNCION MAX 1 SOLO RETURN)

    return mi_archivo
    # except Exception as e:
    #     print(f"Error al cargar el archivo JSON: {e}")
    #     return []
    
def mostrar_puntajes(pantalla, puntajes):
    """
    Muestra una lista de puntajes en terminal.

    """
    fuente = pygame.font.Font(None, 55)
    color_texto = (0, 0, 0)

    x, y = 600, 300
    espaciado = 100

    for i, entrada in enumerate(puntajes):
        texto = f"{i + 1}. {entrada.get('nombre', ' ')}: {entrada.get('puntaje', )}"
        texto_renderizado = fuente.render(texto, True, color_texto)
        pantalla.blit(texto_renderizado, (x, y))
        y += espaciado

puntajes = cargar_puntajes("puntajes.json")
print(puntajes)

def mostrar_pantalla_puntajes_jugadores(pantalla:pygame.Surface, ruta_imagen:str) -> None:
    
    """
    Función para mostrar la pantalla del top de puntajes.

    """

    imagen_ranking = pygame.image.load(ruta_imagen)
    imagen_ranking = pygame.transform.scale(imagen_ranking, pantalla.get_size())
    pantalla.blit(imagen_ranking, (0, 0))

    pygame.display.update()


# Hay que sacar el enumerate --> reemplazar por algo visto en clase.







