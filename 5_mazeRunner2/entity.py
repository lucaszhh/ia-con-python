""" Instancias  """
class Nodo():
    def __init__(self,_estado,_padre,_accion):
        self.estado=_estado   #Entendemos por estado (fila,columna)
        self.padre=_padre     
        self.accion=_accion   #Accion es simplemente un texto
                            #que diga que accion se realizo, ejemplo (Arriba,Abajo,Izquierda,Derecha)
                            #No es fundamental para el funcionamiento
    def __str__(self):
        return(f"\n Nodo:\n Estado:{self.estado}\n Padre: {self.padre} \n Accion:{self.accion}")
    
class FronteraStack():
    def __init__(self):
        self.frontera = []

    def __str__(self):
        return(f"\nEn la frontera se encuentran los nodos: {self.frontera}")

    def agregar_nodo(self,_nodo):
        self.frontera.append(_nodo)
    def quitar_nodo(self):
        return self.frontera.pop()
    def esta_vacia(self):
        return len(self.frontera) == 0
    def contiene_estado(self,_estado):
        return _estado in self.frontera


class FronteraQueue(FronteraStack):
    def quitar_nodo(self):
        return self.frontera.pop(0)

class Laberinto():
    def  __init__(self,_algoritmo):
        '''Dentro del init podemos ejecutar funciones
        para ir definiendo los atributos de la clase.
        Les dejo lista la parte de leer el laberinto
        del archivo de texto, y la detección del inicio,
        meta y paredes.
        '''
        with open('./mazes/maze.txt','r') as archivo:
            contenido=archivo.read()     #Con red() leemos todo el archivo y lo guardamos en contenido
        
        contenido=contenido.splitlines() #Con splitlines() separamos el contenido en lineas, eliminando el \n
        
        self.ancho=len(contenido[0])    #El ancho del laberinto es la cantidad 
                                        #de caracteres de la primer linea 
                                        #(O de cualquiera suponiendo que todas tienen el mismo ancho)
        self.alto=len(contenido)        #El alto del laberinto es la cantidad de lineas
        self.paredes=[]
        self.camino=[]                 #Lista de paredes

        for fila in range(self.alto):   #Recorremos todas las filas
            fila_paredes=[]
            fila_camino=[]             #Creamos una lista vacia para las paredes de la fila actual
                                        #para cada fila se vuelve a limpiar la lista
            for columna in range(self.ancho): #Recorremos todas las columnas
                if contenido[fila][columna]=='#': #Si el caracter es # es una pared
                    fila_paredes.append((fila,columna)) #Agregamos la pared a la lista de paredes de la fila actual
                elif contenido[fila][columna]=='I':   #Si el caracter es I es el inicio
                    self.inicio=(fila,columna)         #Guardamos el inicio
                elif contenido[fila][columna]=='M':   #Si el caracter es M es la meta
                    self.meta=(fila,columna) 
                elif contenido[fila][columna]==' ':
                    fila_camino.append((fila,columna))          #Guardamos la meta
            self.paredes.append(fila_paredes)         #Agregamos la lista de paredes de la fila actual a la lista de paredes
            self.camino.append(fila_camino)         #Agregamos la lista de caminos de la fila actual a la lista de caminos
        #De este modo ya tenemos identificadas las paredes, el inicio y la meta
        self.solucion=None
        self.algoritmo=_algoritmo #String en el que pasamos el nombre del algoritmo a utilizar
        self.nodos_recorridos = set()

    def es_camino(self,_estado):
        i, j = _estado
        
        # Verificar si el nodo está dentro de los límites del laberinto
        if i < 0 or i >= self.alto or j < 0 or j >= self.ancho:
            return False
        
        # Verificar si el nodo es una pared
        for fila_paredes in self.paredes:
            if (i, j) in fila_paredes:
                return False
        
        # Si no es una pared, entonces es un camino válido
        return True


    def expandir_nodo(self,_nodo):

        nodos_candidatos = []
        i, j = _nodo.estado

        arriba = ((i-1,j) , self.es_camino((i-1,j))) 
        derecha = ((i,j +1) ,self.es_camino((i,j +1)))
        abajo = ((i,j - 1 ), self.es_camino((i,j - 1 )))
        izquierda =  ((i + 1, j), self.es_camino((i + 1, j)))

        cordenadas = [arriba,derecha,abajo,izquierda]

        for cordenada in cordenadas :
            if cordenada[1]:
                nodos_candidatos.append(cordenada[0])

        for estado in  nodos_candidatos:
            if _nodo.padre == estado:
                nodos_candidatos.pop(nodos_candidatos.index(estado))

        return nodos_candidatos

    def resolver(self):
            if self.algoritmo=='BFS':
                #Crear la frontera que corresponda
                frontera = FronteraQueue()
            elif self.algoritmo=='DFS':
                #Crear la frontera que corresponda
                frontera = FronteraStack()
            #------------------------------------------------------------------------
            nodo_inicial = Nodo(self.inicio,None,None)
            frontera.agregar_nodo(nodo_inicial)
            self.explorados = set()
            while True:
                if frontera.esta_vacia():
                    print("No hay solucion")
                    return
                nodo_actual = frontera.quitar_nodo()
                self.nodos_recorridos.add(nodo_actual.estado)
                if nodo_actual.estado == self.meta:
                    print(self.meta, "meta")
                    print("Estamos en la meta")
                    return
                self.explorados.add(nodo_actual.estado)
                vecinos = self.expandir_nodo(nodo_actual)
                for vecino in vecinos:
                    if not vecino in self.explorados: 
                        frontera.agregar_nodo(Nodo(vecino,nodo_actual,None))
                
                

