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
                    self.inicio=(fila,columna)         
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
        print("# Paredes \nI Inicio \nM Meta \n+ Solucion")
        print("# Laberinto sin resolver")
        laberinto_str = ""
        for fila in range(self.alto):
            filas = []
            for columna in range(self.ancho):
                filas.append(self.laberinto[fila][columna])
            laberinto_str += "".join(filas) + "\n"
        print(laberinto_str)
        
        print("# Laberinto resuelto")
        laberinto_str = ""
        for fila in range(self.alto):
            filas = []
            for columna in range(self.ancho):
                if self.laberinto[fila][columna] == '#':
                    filas.append("#")
                elif self.laberinto[fila][columna] == 'I':
                    filas.append("I")
                elif self.laberinto[fila][columna] == 'M':
                    filas.append("M")
                elif self.laberinto[fila][columna] == ' ':
                    filas.append(" ")
                
                nodo_actual = None
                for nodo in self.solucion:
                    if nodo.estado == (fila, columna):
                        nodo_actual = nodo
                        break

                if nodo_actual and nodo_actual.estado != self.inicio:
                    filas[columna] = "+"

            laberinto_str += "".join(filas) + "\n"
        print(laberinto_str)
        print(f"Laberinto resuelto por el algoritmo {self.algoritmo}")
        print("**************************************************")

    
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
                print(f"El algoritmo {self.algoritmo} no encontro la solucion")
                return

            nodo_actual = frontera.quitar_nodo()

            if nodo_actual.estado == self.meta:
                print(f"El algoritmo {self.algoritmo} encontro la meta con un total de {len(self.explorados)} nodos explorados")
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