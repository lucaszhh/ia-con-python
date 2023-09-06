import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import Perceptron
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

#Cargar el data set

with open("./pistachio.csv") as archivo:
    lectura = list(csv.reader(archivo))[1:]
    datos = []
    for fila in lectura:
        datos.append({
            "entradas": [fila[i] for i in range(len(fila)-1)],
            "label": fila[-1]
        })

for i in range(5):
    print(datos[i])
