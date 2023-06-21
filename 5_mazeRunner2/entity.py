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
        with open('laberinto.txt','r') as archivo:
            contenido=archivo.read()     #Con red() leemos todo el archivo y lo guardamos en contenido
        
        contenido=contenido.splitlines() #Con splitlines() separamos el contenido en lineas, eliminando el \n
        
        self.ancho=len(contenido[0])    #El ancho del laberinto es la cantidad 
                                        #de caracteres de la primer linea 
                                        #(O de cualquiera suponiendo que todas tienen el mismo ancho)
        self.alto=len(contenido)        #El alto del laberinto es la cantidad de lineas
        self.paredes=[]                 #Lista de paredes

        for fila in range(self.alto):   #Recorremos todas las filas
            fila_paredes=[]             #Creamos una lista vacia para las paredes de la fila actual
                                        #para cada fila se vuelve a limpiar la lista
            for columna in range(self.ancho): #Recorremos todas las columnas
                if contenido[fila][columna]=='#': #Si el caracter es # es una pared
                    fila_paredes.append((fila,columna)) #Agregamos la pared a la lista de paredes de la fila actual
                elif contenido[fila][columna]=='I':   #Si el caracter es I es el inicio
                    self.inicio=(fila,columna)         #Guardamos el inicio
                elif contenido[fila][columna]=='M':   #Si el caracter es M es la meta
                    self.meta=(fila,columna)           #Guardamos la meta
            self.paredes.append(fila_paredes)         #Agregamos la lista de paredes de la fila actual a la lista de paredes
        #De este modo ya tenemos identificadas las paredes, el inicio y la meta
        self.solucion=None
        self.algoritmo=_algoritmo #String en el que pasamos el nombre del algoritmo a utilizar

    def expandir_nodo(self,_nodo):
        '''Dentro de _nodo.estado tenemos la posicion actual del nodo
           Debemos comprobar en todas las direcciones si podemos movernos
           descartando las que sean paredes o esten fuera del laberinto                 (i-1,j)
           Utilicen el grafico que está en el Notion para guiarse                (i,j-1) (i,j) (i,j+1)
           Devolver una lista de vecinos posibles (nodos hijo)                          (i+1,j)
        '''
        pass

    def resolver(self):
        '''
        Acá tienen que implementar el algoritmo de busqueda
        La idea es intentar replicar el pseudocodigo que vimos en clase
        1- Inicializar la frontera con el nodo inicial
        2- Inicializar el conjunto de explorados como vacio
        3- Repetimos:
            3.1- Si la frontera esta vacia, no hay solucion
            3.2- Quitamos un nodo de la frontera
            3.3- Si el nodo contiene un estado que es meta, devolver la solucion
            3.4- Agregar el nodo a explorados
            3.5- Expandir el nodo, agregando los nodos hijos a la frontera
        '''
        if self.algoritmo=='BFS':
            #Crear la frontera que corresponda
            pass
        elif self.algoritmo=='DFS':
            #Crear la frontera que corresponda
            pass
        #------------------------------------------------------------------------
        pass
