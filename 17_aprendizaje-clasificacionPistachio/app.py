import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import Perceptron
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# Cargar el dataset
with open("./pistachio.csv") as archivo:
    lectura = list(csv.reader(archivo))[1:]
    datos = []
    for fila in lectura:
        datos.append({
            'entradas' : [float(fila[i]) for i in range(len(fila) - 1)],
            'label': "Kirmizi" if fila[-1] == 'Kirmizi_Pistachio' else "Siit"
        })


X_train, X_test, y_train, y_test = train_test_split(
    [dato['entradas'] for dato in datos],
    [dato['label'] for dato in datos],
    test_size=0.2        # Recuerden que mayor porcentaje para entrenamiento es mejor
)

# Pueden cambiar el modelo y utilizar cualquiera de los que vimos en clase
# prueben con los 3 y vean cual les da mejores resultados

# modelo = Perceptron()
modelo = SVC()
# modelo = KNeighborsClassifier(n_neighbors=3)

# Entrenamos el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

# Generamos las predicciones para los datos de prueba que separamos antes
predicciones = modelo.predict(X_test)

# Evaluamos la precision del modelo contando el numero de aciertos y errores
correcto = (y_test == predicciones).sum()
incorrecto = (y_test != predicciones).sum()
total = len(predicciones)

print(f"Numero de datos en el dataset: {len(datos)}")
print(f"Proporcion de datos para entrenamiento: {len(X_train) / len(datos):.2f}")
print("--------------------------------------------------")
print(f"Resultados para el modelo {type(modelo).__name__}")
print(f"Correcto: {correcto}")
print(f"Incorrecto: {incorrecto}")
print(f"Exactitud: {100 * correcto / total:.2f}%")

# Pueden hacer nuevas predicciones
prediccion_n = modelo.predict([[68539,1078.8311,445.5626,197.1964,0.8967,295.4091,0.9815,69829,0.7889,2.2595,0.74,0.663,0.0065,0.0029,0.4396,0.9932]])
print(f"Prediccion: {prediccion_n}")