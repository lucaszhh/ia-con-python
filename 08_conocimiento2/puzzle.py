from logic import *

personas = ["Pedro", "Clara", "Franco", "Lucia"]
equipos = ["Boca", "River", "Independiente", "Racing"]

symbols = []

knowledge = And()

for persona in personas:
    for equipo in equipos:
        symbols.append(Symbol(f"{persona}{equipo}"))

# cada persona hincha por un equipo
for persona in personas:
    knowledge.add(Or(
        Symbol(f"{persona}Boca"),
        Symbol(f"{persona}River"),
        Symbol(f"{persona}Independiente"),
        Symbol(f"{persona}Racing")
    ))

# solo un equipo por persona
for persona in personas:
    for h1 in equipos:
        for h2 in equipos:
            if h1 != h2:
                knowledge.add(
                    Implication(Symbol(f"{persona}{h1}"), Not(Symbol(f"{persona}{h2}")))
                )

# solo una persona por equipo
for equipo in equipos:
    for p1 in personas:
        for p2 in personas:
            if p1 != p2:
                knowledge.add(
                    Implication(Symbol(f"{p1}{equipo}"), Not(Symbol(f"{p2}{equipo}")))
                )

knowledge.add(
    Or(Symbol("PedroBoca"), Symbol("PedroIndependiente"))
)

knowledge.add(
    Not(Symbol("ClaraRacing"))
)

knowledge.add(
    Symbol("FrancoBoca")
)

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)
