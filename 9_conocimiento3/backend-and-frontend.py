""" 
ACTIVIDAD CONOCIMIENTO
En una isla remota, hay dos tipos de habitantes: BackEnd developer (back) y FrontEnd developer (front). Los FrontEnd siempre dicen la verdad, mientras que los ladrones siempre mienten.

Un día, te encuentras con tres habitantes de la isla, A y B (y C), pero no sabes quién es quién. Quieres averiguar qué tipo de habitante es cada uno de ellos:

Primer escenario:
A dice: “Soy un FrontEnd y un BackEnd”

Segundo escenario:
A dice: “Ambos somos Backend”
B no dice nada

Tercer escenario:
A dice: “Somos del mismo tipo”
B dice: “Somos de distintos tipos”

Cuarto escenario:
A dice: “Soy un FrontEnd” o “Soy un BackEnd” (pero no sabemos cuál frase dijo)
B dice: “A dijo ‘Soy un BackEnd’ ”
B luego dice: “C es un BackEnd”
C dice “A es un FrontEnd”

"""
from logic import *

developers = ["Front", "Back"]
personas = ["A", "B", "C"]

symbols = {}


for persona in personas:
    for dev in developers:
        atribute = dev+persona
        symbols[atribute] = Symbol(f"{dev}{persona}")
        
print(symbols,"symbols")

""" 
Primer escenario:
A dice: “Soy un FrontEnd y un BackEnd” 
"""
knowledge1 = And(symbols["FrontA"], symbols["BackA"])
""" knowledge1 = And(Symbol("FrontA"), Symbol("BackA")) """

print(knowledge1.formula())
print(model_check(knowledge1,symbols["BackA"]))



