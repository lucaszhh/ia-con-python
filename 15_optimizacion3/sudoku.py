from constraint import AllDifferentConstraint, Problem

# Crear un problema de restricciones
problem = Problem()

# Definir variables y dominios
# Usaremos números del 1 al 9 para representar las celdas vacías
# 0 representará las celdas en blanco
for row in range(9):
    for col in range(9):
        problem.addVariable((row, col), list(range(1, 10)))

# Restricciones por filas
for row in range(9):
    problem.addConstraint(AllDifferentConstraint(), [(row, col) for col in range(9)])

# Restricciones por columnas
for col in range(9):
    problem.addConstraint(AllDifferentConstraint(), [(row, col) for row in range(9)])

# Restricciones por cuadrados de 3x3
for row_block in range(3):
    for col_block in range(3):
        cells = [(row_block * 3 + i, col_block * 3 + j) for i in range(3) for j in range(3)]
        problem.addConstraint(AllDifferentConstraint(), cells)

# Inserta los valores conocidos (números iniciales del Sudoku)
known_values = {
    (0, 2): 5, (0, 3): 1, (0, 8): 7,
    (1, 1): 9, (1, 4): 7, (1, 7): 8,
    (2, 0): 2, (2, 5): 4,
    (3, 0): 5, (3, 3): 9, (3, 4): 1, (3, 5): 7, (3, 7): 6, (3, 8): 3,
    (4, 0): 8, (4, 2): 6, (4, 6): 4, (4, 8): 1,
    (5, 0): 3, (5, 1): 7, (5, 2): 4, (5, 5): 8, (5, 8): 5,
    (6, 3): 8, (6, 4): 5, (6, 6): 9,
    (7, 1): 5, (7, 4): 9, (7, 7): 3,
    (8, 0): 7, (8, 5): 1, (8, 6): 8
}

for cell, value in known_values.items():
    problem.addConstraint(lambda var, value=value: var == value, [cell])

# Encuentra una solución
solutions = problem.getSolutions()

if solutions:
    solution = solutions[0]
    for row in range(9):
        for col in range(9):
            print(solution[(row, col)], end=" ")
        print()
else:
    print("No se encontró una solución válida.")
