import pygame
import sys
import time

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


""" Funciones de dibujo """

def DIBUJAR_CUADRADO(x, y, color):
    pygame.draw.rect(PANTALLA, NEGRO, (x, y, 20, 20))
    pygame.draw.rect(PANTALLA, color, (x, y, 18, 18))


def DIBUJAR_META (nodos_solucion):
    pygame.draw.polygon(PANTALLA, VERDE1,  nodos_solucion, 5)

def DIBUJAR_FILA(y,filas):
    POSICIONX = 20
    for cuadrado in filas:
        if cuadrado == "#":
            DIBUJAR_CUADRADO(POSICIONX, y, NEGRO )
        elif cuadrado == "M":
            DIBUJAR_CUADRADO(POSICIONX, y, VERDE1 )
        elif cuadrado == "I":
            DIBUJAR_CUADRADO(POSICIONX, y, VERDE1 )
        elif cuadrado == " ":
            DIBUJAR_CUADRADO(POSICIONX, y, GRIS)
        POSICIONX += 20



class Nodo():
    def __init__(self, _estado, _padre, distancia):
        self.estado = _estado
        self.padre = _padre
        self.distancia = distancia

class FronteraStack():
    def __init__(self):
        self.frontera=[]
    def agregar_nodo(self,_nodo):
        self.frontera.append(_nodo)
    def quitar_nodo(self):
        return self.frontera.pop()
    def esta_vacia(self):
        return len(self.frontera)==0
    
    def contiene_estado(self,_estado):
        for nodo in self.frontera:
            if nodo.estado == _estado:
                return True
        return False

class FronteraQueue(FronteraStack):
    def quitar_nodo(self):
        return self.frontera.pop(0)

class FronteraDistancia(FronteraQueue):
    def quitar_nodo(self):
        self.frontera = sorted(self.frontera, key=lambda x: x.distancia)
        return self.frontera.pop(0)

class Laberinto():
    def  __init__(self,_algoritmo, _path):
        with open(_path,'r') as archivo:
            laberinto=archivo.read()    
        self.laberinto=laberinto.splitlines() 
        self.ancho=len(self.laberinto[0])                                  
        self.alto=len(self.laberinto)       
        self.paredes=[]  
        self.solucion = []
        self.algoritmo=_algoritmo               

        for fila in range(self.alto):   
            fila_paredes=[]             
            for columna in range(self.ancho): 
                if self.laberinto[fila][columna]==' ': 
                    fila_paredes.append(False) 
                elif self.laberinto[fila][columna]=='I':   
                    self.inicio=(fila,columna)  # Mover esta línea fuera del bucle         
                    fila_paredes.append(False)
                elif self.laberinto[fila][columna]=='M':   
                    self.meta=(fila,columna)
                    fila_paredes.append(False)
                else:
                    fila_paredes.append(True)
            self.paredes.append(fila_paredes)

    def tomar_distancia(self,estado):
        x1, y1 = estado
        x2, y2 = self.meta
        dixt_y = abs(y2 - y1)
        dixt_x = abs(x2 - x1)
        return dixt_x + dixt_y
    
    def dibujar_solucion(self):
        for fila in range(self.alto):
            filas = []
            for columna in range(self.ancho):
                filas.append(self.laberinto[fila][columna])
            DIBUJAR_FILA((fila + 1) * 20, filas)
            print(filas, "filas")
        for nodo in self.solucion:
            time.sleep(0.2)
            DIBUJAR_CUADRADO((nodo.estado[1] * 20) + 20, (nodo.estado[0] + 1) * 20, VERDE1)
            pygame.display.update()

    def expandir_nodo(self,_nodo):
        fila, columna = _nodo.estado
        vecinos = []
        candidatos = [(fila-1,columna),(fila,columna-1),(fila,columna+1),(fila+1,columna)]
        
        for f,c in candidatos:
            if 0 <= f < self.alto and 0 <= c < self.ancho and not self.paredes[f][c]:
                vecinos.append((f,c))
        return vecinos

    def resolver(self):
        if self.algoritmo == 'BFS':
            frontera = FronteraQueue()
        elif self.algoritmo == 'DFS':
            frontera = FronteraStack()
        elif self.algoritmo == 'GBFS' or self.algoritmo == 'A*':
            frontera = FronteraDistancia()

        nodo_inicial = Nodo(self.inicio, None, 0)
        frontera.agregar_nodo(nodo_inicial)
        self.explorados = set()

        while True:
            if frontera.esta_vacia():
                print(f"El algoritmo {self.algoritmo} no encontró la solución")
                return

            nodo_actual = frontera.quitar_nodo()

            if nodo_actual.estado == self.meta:
                print(f"El algoritmo {self.algoritmo} encontró la meta con un total de {len(self.explorados)} nodos explorados")
                while nodo_actual.padre is not None:
                    self.solucion.append(nodo_actual.padre)
                    nodo_actual = nodo_actual.padre
                self.solucion.reverse()
                self.dibujar_solucion()
                return self.solucion

            self.explorados.add(nodo_actual.estado)
            vecinos = self.expandir_nodo(nodo_actual)

            for vecino in vecinos:
                if not frontera.contiene_estado(vecino) and vecino not in self.explorados:
                    costo = nodo_actual.distancia + 1  # Costo del padre más 1
                    if self.algoritmo == 'GBFS':
                        distancia = self.tomar_distancia(vecino)
                        nodo_hijo = Nodo(vecino, nodo_actual, distancia)
                    elif self.algoritmo == 'A*':
                        distancia = self.tomar_distancia(vecino)
                        heuristica = distancia + costo
                        nodo_hijo = Nodo(vecino, nodo_actual, heuristica)
                    else:
                        nodo_hijo = Nodo(vecino, nodo_actual, costo)

                    frontera.agregar_nodo(nodo_hijo)

                    print(costo, "costo")


""" import laberintos """
laberintoTxt = "./laberintos/laberinto.txt"
laberintoTxt1 = "./laberintos/laberinto1.txt"
laberintoTxt2 = "./laberintos/laberinto2.txt"
laberintoTxt3 = "./laberintos/laberinto3.txt"

""" Posibles algoritmos BFS DFS GBFS A* """

Laberinto("A*", laberintoTxt).resolver()


""" Bucle que permite que la página no se cierre """
""" while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update() """