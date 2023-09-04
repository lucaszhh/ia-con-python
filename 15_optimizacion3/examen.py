from constraint import * # import de la libreria python-constraint

problema = Problem()

problema.addVariables(
    ["A","B","C","D","E","F","G"], # variables
    ["Lunes","Martes","Miércoles"] # dominios
)

# todas las restricciones posibles
RESTRICCIONES = [
    ("A","B"),
    ("A","C"),
    ("B","C"),
    ("B","D"),
    ("B","E"),
    ("C","E"),
    ("C","F"),
    ("D","E"),
    ("E","F"),
    ("E","G"),
    ("F","G"), 
]

for x, y in RESTRICCIONES:
    problema.addConstraint(lambda x,y: x != y, (x,y)) # añado cada una de las restricciones de a una con una función lambda

for solucion in problema.getSolutions():
    print(solucion)