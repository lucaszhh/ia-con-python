from entity import *

print("***************** MI APP *******************")

""" nodo_1 = (1,1)
nodo_2 = (1,2)
nodo_3 = (1,3)

mi_first_nodo = Nodo(nodo_1,nodo_2,"none")

mi_first_stack = FronteraStack()

mi_first_stack.agregar_nodo(nodo_1)
mi_first_stack.agregar_nodo(nodo_2)
mi_first_stack.agregar_nodo(nodo_3)
print("stak",mi_first_stack) 
print(mi_first_stack.quitar_nodo())
print("stak",mi_first_stack) 
print("esta_vacia",mi_first_stack.esta_vacia())
print(mi_first_stack.quitar_nodo())
print(mi_first_stack.quitar_nodo())
print("contiene estado",mi_first_stack.contiene_estado(nodo_1))
print("esta_vacia",mi_first_stack.esta_vacia()) """

print("******************************************************")
print("******************************************************")

""" mi_first_queue = FronteraQueue()

print("queue",mi_first_queue)

mi_first_queue.agregar_nodo(nodo_1)
mi_first_queue.agregar_nodo(nodo_2)
mi_first_queue.agregar_nodo(nodo_3)
print("stak",mi_first_queue) 
print(mi_first_queue.quitar_nodo())
print("stak",mi_first_queue) 
print("esta_vacia",mi_first_queue.esta_vacia())
print(mi_first_queue.quitar_nodo())
print(mi_first_queue.quitar_nodo())
print("contiene estado",mi_first_queue.contiene_estado(nodo_1))
print("esta_vacia",mi_first_queue.esta_vacia())
"""

print("******************************************************")
print("******************************************************")
""" LABERINTO """
Laberinto1 = Laberinto("DFS")


print(Laberinto1.inicio, "inicio")
Laberinto1.resolver()
print(len(Laberinto1.nodos_recorridos), "nodos_recorridos")
""" print(Laberinto1.nodos_recorridos, "nodos_recorridos") """

""" print(Laberinto1.camino,"camino") """

concatenado = []

for array in Laberinto1.camino:
    concatenado.extend(array)

""" print(concatenado) """

print(len(concatenado), "nodos camino")
print("dibujar camino", Laberinto1.dibujar_solucion())