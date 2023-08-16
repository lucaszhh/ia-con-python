from logic import *

mostaza = Symbol("CorMostaza")
moradillo = Symbol("ProfMor")
escarlata = Symbol("Escarlata")
personajes = [mostaza, moradillo, escarlata]

baile = Symbol("baile")
cocina = Symbol("cocina")
libreria = Symbol("libreria")
habitaciones = [baile, cocina, libreria]

cuchillo = Symbol("cuchillo")
revolver = Symbol("revolver")
llave = Symbol("llave")
armas = [cuchillo, revolver, llave]

symbols = personajes + habitaciones + armas


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(f"{symbol}: SI")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: QUIZAS")


# Solo puede haber una persona, una habitacion y un arma
knowledge = And(
    Or(mostaza, moradillo, escarlata),
    Or(baile, cocina, libreria),
    Or(cuchillo, revolver, llave)
)

# Cartas iniciales
knowledge.add(And(
    Not(mostaza), Not(cocina), Not(revolver)
))

# Informacion que se pero aun no compruebo
knowledge.add(Or(
    Not(escarlata), Not(libreria), Not(llave)
))

# Acusaciones
knowledge.add(Not(moradillo))
knowledge.add(Not(baile))

check_knowledge(knowledge)