from pgmpy.models import BayesianNetwork 
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Como crear una tabla ?
# Creacion de la tabla de probabilidad de lluvia

lluvia = "lluvia"
mantenimiento = "mantenimiento"
tren = "tren"
reunion = "reunion"

red_bayes = BayesianNetwork([(lluvia,mantenimiento),(lluvia,tren),(mantenimiento,tren),(tren,reunion)])

lluvia_cpd = TabularCPD(variable=lluvia, variable_card=3, values=[[0.7],[0.2],[0.1]], state_names={lluvia:["nula","ligera","fuerte"]})

# Otra forma de crear una tabla sin tanto hardcodeo
# Creacion de la tabla de probabilidad de mantenimiento dado lluvia

mantenimiento_list =  {"si": [0.4,0.2,0.1], "no": [0.6,0.8,0.9]}

lluvia_cpd = TabularCPD(
    variable = mantenimiento,
    variable_card = len(mantenimiento_list.keys()),
    values=[mantenimiento_list[key] for key in mantenimiento_list.keys()],
    evidence = [lluvia],
    evidence_card = [3],
    state_names= {
        mantenimiento: list(mantenimiento_list.keys()),
        lluvia:["nula","ligera","fuerte"] 
    }
)

# Creacion de la tabla de probabilidad de tren dado lluvia y mantenimiento

tren_list = {"a_tiempo": [0.8,0.9,0.6,0.7,0.4,0.5] , "demorado": [0.2,0.1,0.4,0.3,0.6,0.5]}

tren_cpd = TabularCPD(
    variable=tren,
    variable_card= len(tren_list.keys()),
    values= [tren_list[key] for key in tren_list.keys()],
    evidence=[lluvia,mantenimiento],
    evidence_card=[3,2],
    state_names={
        tren: list(tren_list.keys()),
        mantenimiento: list(mantenimiento_list.keys()),
        lluvia:["nula","ligera","fuerte"] 
    }
)

print(tren_cpd)

# Creacion de la tabla de probabilidad de reunion dado tren

reunion_list = {"asistir": [0.9,0.6], "no_asistir":[0.1,0.4]}

reunion_cpd = TabularCPD(
    variable=reunion,
    variable_card= len(reunion_list.keys()),
    values=[reunion_list[key] for key in reunion_list.keys()],
    evidence=[tren],
    evidence_card=[2],
    state_names={
        tren: list(tren_list.keys()),
        reunion : list(reunion_list.keys())
    }
)

print(reunion_cpd)









