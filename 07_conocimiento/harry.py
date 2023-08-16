from logic import *

lluvia = Symbol("lluvia")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")

knowledge = And(
    Implication(Not(lluvia), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)
#print(knowledge.formula())
print(model_check(knowledge, dumbledore and lluvia))