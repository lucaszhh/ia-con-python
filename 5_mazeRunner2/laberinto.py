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
Laberinto1 = Laberinto("BFS")

""" print(Laberinto1.paredes, "paredes")
print(Laberinto1.camino, "camino")
print(Laberinto1.algoritmo, "algoritmo")
print(Laberinto1.alto, "alto")
print(Laberinto1.ancho, "ancho")
print(Laberinto1.inicio, "inicio")
print(Laberinto1.meta, "meta")
print(Laberinto1.solucion, "solucion") """

Laberinto1.resolver()