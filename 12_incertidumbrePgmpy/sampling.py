from red_bayesiana import *
from pgmpy.sampling import BayesianModelSampling

#  Sampling aleatorio de multiples probabilidades
inferencia = BayesianModelSampling(red_bayes)
muestras = inferencia.forward_sample(size=100000)

# print(muestras)

# Samplin de muestras marginales probabilidad unica
marginales = muestras[mantenimiento].value_counts(normalize=True).reset_index()
marginales.columns = ["estado", "probabilidad"]

print(marginales)


