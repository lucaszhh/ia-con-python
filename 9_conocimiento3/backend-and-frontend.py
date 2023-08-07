""" 
ACTIVIDAD CONOCIMIENTO
En una isla remota, hay dos tipos de habitantes: BackEnd developer (back) y FrontEnd developer (front). Los FrontEnd siempre dicen la verdad, mientras que los ladrones siempre mienten.

Un día, te encuentras con tres habitantes de la isla, A y B (y C), pero no sabes quién es quién. Quieres averiguar qué tipo de habitante es cada uno de ellos:
"""

from logic import *

developers = ["Front", "Back"]
personas = ["A", "B", "C"]

symbols = {}
symbols_list = []


for persona in personas:
    for dev in developers:
        atribute = dev+persona
        symbols[atribute] = Symbol(f"{dev}{persona}")
        symbols_list.append(Symbol(f"{dev}{persona}"))
        
print(symbols,"symbols")

""" 
    Primer escenario:
    A dice: “Soy un FrontEnd y un BackEnd” 
"""

# Rules
knowledge1 = And(
    Or(symbols["FrontA"], symbols["BackA"]), # Es front o es back
    Not(And(symbols["FrontA"], symbols["BackA"])), # No pueden ser front y back a la vez
)

# Conocimiento
knowledge1.add(
    Implication(
        symbols["FrontA"], 
        And(symbols["FrontA"], symbols["BackA"]))
)
knowledge1.add(
    Implication(
        symbols["BackA"], 
        Not(And(symbols["FrontA"], symbols["BackA"])))
)

# Logs
print("knowledge1")
for symbol in symbols_list:
    if model_check(knowledge1, symbol):
        print(f"{symbol}")


""" 
    Segundo escenario:
    A dice: “Ambos somos Backend”
    B no dice nada 
"""

# Rules
knowledge2 = And(
    # A
    Or(symbols["FrontA"], symbols["BackA"]), # Es front o es back
    Not(And(symbols["FrontA"], symbols["BackA"])), # No pueden ser front y back a la vez
    
    # B
    Or(symbols["FrontB"], symbols["BackB"]), # Es front o es back
    Not(And(symbols["FrontB"], symbols["BackB"])), # No pueden ser front y back a la vez
)

# Conocimiento
knowledge2.add(
    Implication(
        symbols["FrontA"], 
        And(symbols["BackA"],symbols["BackB"])
    )
)
knowledge2.add(
    Implication(
        symbols["BackA"], 
        Not(And(symbols["BackA"],symbols["BackB"]))
    )
)


# Logs
print("knowledge2")
for symbol in symbols_list:
    """ print(model_check(knowledge2, symbol)) """
    if model_check(knowledge2, symbol):
        print(f"{symbol}")


""" 
    Tercer escenario:
    A dice: “Somos del mismo tipo”
    B dice: “Somos de distintos tipos”
"""

# Rules
knowledge3 = And(
    # A
    Or(symbols["FrontA"], symbols["BackA"]), # Es front o es back
    Not(And(symbols["FrontA"], symbols["BackA"])), # No pueden ser front y back a la vez
    
    # B
    Or(symbols["FrontB"], symbols["BackB"]), # Es front o es back
    Not(And(symbols["FrontB"], symbols["BackB"])), # No pueden ser front y back a la vez
)

# Conocimiento
knowledge3.add(
    Implication(
        symbols["FrontA"],
        And(symbols["FrontA"],symbols["FrontB"])
    )
)
knowledge3.add(
    Implication(
        symbols["BackA"],
        Not(And(symbols["BackA"],symbols["BackB"]))
    ),
)
knowledge3.add(
    Implication(
        symbols["FrontB"],
        symbols["BackA"]
    ),
)
knowledge3.add(
    Implication(
        symbols["BackB"],
        Not(symbols["FrontA"])
    ),
)


# Logs
print("knowledge3")
for symbol in symbols_list:
    if model_check(knowledge3, symbol):
        print(f"{symbol}")

"""
    Cuarto escenario:
    A dice: “Soy un FrontEnd” o “Soy un BackEnd” (pero no sabemos cuál frase dijo)
    B dice: “A dijo ‘Soy un BackEnd’ ”
    B luego dice: “C es un BackEnd”
    C dice “A es un FrontEnd”
"""

# Rules
knowledge4 = And(
    # A
    Or(symbols["FrontA"], symbols["BackA"]), # Es front o es back
    Not(And(symbols["FrontA"], symbols["BackA"])), # No pueden ser front y back a la vez
    
    # B
    Or(symbols["FrontB"], symbols["BackB"]), # Es front o es back
    Not(And(symbols["FrontB"], symbols["BackB"])), # No pueden ser front y back a la vez
    
    # C
    Or(symbols["FrontC"], symbols["BackC"]), # Es front o es back
    Not(And(symbols["FrontC"], symbols["BackC"])), # No pueden ser front y back a la vez
)

# Conocimiento
# B dice: “A dijo ‘Soy un BackEnd’ ”
knowledge4.add(
    Implication(
        symbols["FrontB"], And(Implication(symbols["FrontA"], symbols["FrontB"]), Implication(symbols["FrontB"], Not(symbols["FrontB"])))
    )
)
knowledge4.add(
    Implication(
        symbols["BackB"], Not(And(Implication(symbols["FrontA"], symbols["FrontB"]), Implication(symbols["FrontB"], Not(symbols["FrontB"]))))
    )
)
# B luego dice: “C es un BackEnd”
knowledge4.add(
    Implication(
        symbols["FrontB"], symbols["BackC"]
    )
)
knowledge4.add(
    Implication(
        symbols["BackB"], Not(symbols["BackC"])
    )
)
# C dice “A es un FrontEnd”
knowledge4.add(
    Implication(
        symbols["FrontC"], symbols["FrontA"]
    )
)
knowledge4.add(
    Implication(
        symbols["BackC"], Not(symbols["FrontA"])
    )
)

# Logs
print("knowledge4")
for symbol in symbols_list:
    if model_check(knowledge4, symbol):
        print(f"{symbol}")

