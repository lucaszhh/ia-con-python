from logic import *

colores = ["rojo", "azul", "verde", "amarillo"]

symbols = []

for i in range(4):
    for color in colores:
        symbols.append(Symbol(f"{color}{i}"))

knowledge = And()

# Cada color tiene una posicion
for color in colores:
    knowledge.add(Or(
        Symbol(f"{color}0"),
        Symbol(f"{color}1"),
        Symbol(f"{color}2"),
        Symbol(f"{color}3")
    ))

# Una posicion por color
for color in colores:
    for i in range(4):
        for j in range(4):
            if i != j:
                knowledge.add(Implication(
                    Symbol(f"{color}{i}"), Not(Symbol(f"{color}{j}"))
                ))

# Solo un color por posicion
for i in range(4):
    for c1 in colores:
        for c2 in colores:
            if c1 != c2:
                knowledge.add(Implication(
                    Symbol(f"{c1}{i}"), Not(Symbol(f"{c2}{i}"))
                ))

knowledge.add(Or(
    And(Symbol("rojo0"), Symbol("azul1"), Not(Symbol("verde2")), Not(Symbol("amarillo3"))),
    And(Symbol("rojo0"), Symbol("verde2"), Not(Symbol("azul1")), Not(Symbol("amarillo3"))),
    And(Symbol("rojo0"), Symbol("amarillo3"), Not(Symbol("azul1")), Not(Symbol("verde2"))),
    And(Symbol("azul1"), Symbol("verde2"), Not(Symbol("rojo0")), Not(Symbol("amarillo3"))),
    And(Symbol("azul1"), Symbol("amarillo3"), Not(Symbol("rojo0")), Not(Symbol("verde2"))),
    And(Symbol("verde2"), Symbol("amarillo3"), Not(Symbol("rojo0")), Not(Symbol("azul1")))
))
print(knowledge.formula())
knowledge.add(And(
    Not(Symbol("azul0")),
    Not(Symbol("rojo1")),
    Not(Symbol("verde2")),
    Not(Symbol("amarillo3"))
))

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)