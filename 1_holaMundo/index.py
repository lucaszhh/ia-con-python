""" Saludo cordial """
print("Nola Mundo")

""" Saludo cordial n veces """

def saludo_cordial(n):
   for i in range(n):
      print("Hola mundo")

saludo_cordial(5)

""" Selección numero mayor en una lista """
def maximo_en_lista():
    lista = [1,3,5,7,11,13]
    maximo = lista[0]
    for numero in lista:
       if lista[numero - 1] > maximo:
          maximo = lista[numero -1]
    print("El numero mas grande de la lista es: "+ str(maximo))

maximo_en_lista()