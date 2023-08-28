import scipy.optimize as spo

def calcular_solucion(solucion):
    if solucion.success:
        print(f"X1: {round(solucion.x[0],2)} unidades")
        print(f"X2: {round(solucion.x[1],2)} unidades")
        print(f"cost: {-solucion.fun}$")
    else:
        print("sin solucion")

solucion = spo.linprog(
    [50,80], #funcion de coste: 50x_1 + 80x_2 el coste es negativo por que buscamos minimizar
    A_ub=[[5,2],[-10,-12]], #coeficientes para las desigualdades
    b_ub=[20,-90],   #resticciones para las desigualdades: 20 y 90
)

calcular_solucion(solucion)


""" ************************ """

solucion2 = spo.linprog(
    [-15,-10], # funcion de coste 15L_1 + 10L_2 el coste es negativo por que buscamos maximizar
    A_ub=[[20/60, 30/60], [20/60, 10/60]], 
    b_ub=[100,80]
)

calcular_solucion(solucion2)

""" 
Desafio ejemplo
Con el comienzo del curso se va a lanzar unas ofertas de material escolar. 
Unos almacenes quieren ofrecer 600 cuadernos, 500 carpetas y 400 bolígrafos para la oferta, 
empaquetándolo de dos formas distintas; en el primer bloque pondrá 2 cuadernos, 1 carpeta y 2 bolígrafos; 
en el segundo, pondrán 3 cuadernos, 1 carpeta y 1 bolígrafo. Los precios de cada paquete serán 6.5 y 7 €, 
respectivamente. ¿Cuántos paquetes le conviene poner de cada tipo para obtener el máximo beneficio?
"""