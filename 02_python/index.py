# -*- coding: utf-8 -*-

""" variables """
print("VARIABLES")

a = 23
b = "Mundo"
c = "Hola"

print(a)
print(b)
print(c)


print(f"hola mundo soi lucas y tengo {a} años")
print(c,b)


""" constantes """
print("CONSTANTES")

PI = 3.14
VELOCIDAD_LUZ = 299792458

print("pi",PI,"velocidad de la luz",VELOCIDAD_LUZ)

""" listas y metodos """
print("LISTAS")

numeros = [1,2,3,4,5]
autos = ["Mazda","Toyota","Honda","Ford"]
mixto = [5.5,10,"Texto",False]

print(numeros)
print(autos)
print(mixto)

numeros.append(6)
numeros.remove(3)
autos.insert(1,"Chevrolet")
mixto.pop()

print(numeros)
print(autos)
print(mixto)

lista = [1, 2, 3, 4, 5]
lista += [6, 7, 8, 9, 10]
print(lista)
lista.extend([11, 12, 13, 14, 15])
print(lista)

lista_1 = [1, 2, 3, 4, 5]
lista_2 = lista_1.copy()
lista_3 = list(lista_2)

lista_modificada = lista_1
lista_modificada[0] = 10    # También modifica lista_1

lista_2[0] = 20             # No modifica lista_1

print("Lista 1:",lista_1,"Lista modificada:",lista_modificada)

print("Lista 2:",lista_2,"Lista 3:",lista_3)

lista_con_indice = ["a","b","c","d"]
for indice,valor in enumerate(lista_con_indice):
    print(f"El valor de la lista es: {valor} y tiene un indice igual a: {indice}")

""" 
Otra operacion que podemos realizar con las listas es cortarlas. Para ello utilizamos el operador **[ inicio : final : paso ]**.
  
*En caso de iniciar en 0, finalizar en el último elemento o utilizar paso 1, podemos omitirlos.*
  
El final no es inclusivo, es decir, el elemento del índice final no se incluye en la lista resultante.

Ejemplos """

mi_lista = [10,20,30,40,50]
mi_lista_cortada = mi_lista[1:4]
print(mi_lista[:3])
print(mi_lista[2:4])
print(mi_lista_cortada)
print("Mi lista al revés:",mi_lista[::-1])


"""  matrices """
print("MATRICES")


matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(matriz[0][0])
print(matriz[2][2])
matriz[1][1] = 10
print(matriz[1][1])
print(matriz)


""" tuplas """
print("TUPLA")
mi_primer_tupla = (1,2,3,4,5,6)
print(mi_primer_tupla)

""" diccionario """
print("DICCIONARIO")

alumno_1 = {"nombre":"Juan","apellido":"Perez","edad":25}
alumno_2 = dict(nombre="Jose",apellido="Martinez",edad=40)
print("El alumno 1 se llama",alumno_1["nombre"],alumno_1["apellido"],"y tiene",alumno_1["edad"],"años")
print("El alumno 2 se llama",alumno_2["nombre"],alumno_2["apellido"],"y tiene",alumno_2["edad"],"años")

nombre_alumno_1 = alumno_1.get("nombre")
print(nombre_alumno_1)

""" estructuras de control """
print("ESTRUCTURAS DE CONTROL")

numero_1 = 11
numero_2 = 3

if numero_1 > numero_2:
    print("El número 1 es mayor")
elif numero_1 < numero_2:
    print("El número 2 es mayor")
else:
    print("Los números son iguales")

