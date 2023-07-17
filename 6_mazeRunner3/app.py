import pygame, sys
from entities import Laberinto

""" Paleta de colores """
BLANCO = (255,255,255)
NEGRO = (0,0,0)
VERDE1 = (55,148,73)
GRIS = (22,22,22)

""" Inizializador de pantalla y de pygame"""
pygame.init()
PANTALLA =  pygame.display.set_mode((1000,500))
pygame.display.set_caption("MAZE") #nombre de la pantalla
PANTALLA.fill(BLANCO) # seteo del color de la pantalla

""" Perzonalizacion del icono de la pantalla """
ICON = pygame.image.load("./images/maze.png")
pygame.display.set_icon(ICON)

""" import laberintos """
laberintoTxt = "./laberintos/laberinto.txt"
laberintoTxt1 = "./laberintos/laberinto1.txt"
laberintoTxt2 = "./laberintos/laberinto2.txt"
laberintoTxt3 = "./laberintos/laberinto3.txt"

""" Posibles algoritmos BFS DFS GBFS A* """

Laberinto("BFS", laberintoTxt3).resolver()
Laberinto("DFS", laberintoTxt3).resolver()
Laberinto("GBFS", laberintoTxt3).resolver()
Laberinto("A*", laberintoTxt3).resolver()

""" Funciones de dibujo """

def DIBUJAR_CUADRADO (x,y,color):
    pygame.draw.rect(PANTALLA, color,(x,y,20,20))

def DIBUJAR_META (nodos_solucion):
    pygame.draw.polygon(PANTALLA, VERDE2,  nodos_solucion, 5)

def DIBUJAR_FILA(y,filas):
    for cuadrado in filas:
        POSICIONX = 20
        if cuadrado == "#":
            DIBUJAR_CUADRADO(POSICIONX, y, NEGRO )
        elif cuadrado == "M":
            DIBUJAR_CUADRADO(POSICIONX, y, VERDE1 )
        elif cuadrado == "I":
            DIBUJAR_CUADRADO(POSICIONX, y, VERDE1 )
        else:
            DIBUJAR_CUADRADO(POSICIONX, y, GRIS)
        POSICIONX += 20


""" Bucle que permite que la página no se cierre """
while True:
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            sys.exit()
    pygame.display.update() #funcion que permite que se actualice la pantalla 