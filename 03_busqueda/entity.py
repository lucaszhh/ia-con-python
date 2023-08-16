""" Instancia de la clase """
class Alumno:
    """ Declaración función constructora """
    def __init__ (self, _nombre, _apellido, _edad ) :
        self.nombre = _nombre
        self.apellido = _apellido
        self.edad = _edad

    """ Declaración de funciones de la instancia de la clase """
    def estudiar(self):
        print("Estudiandooo...")

    def estudiarMateria(self, _materia):
        print(f"Estoy estudiando {_materia}")

    def presentarse(self):
        print(f"Hola soy {self.nombre} {self.apellido} y tengo {self.edad} anios ")

""" ******************************************************************************* """

""" Instancia de la clase a partir de la clase Alumno """
""" Herencia """
class AlumnoEspecial(Alumno):
    """ Declaración función constructora """
    def __init__ (self, _nombre, _apellido, _edad ) :
        self.nombre = _nombre
        self.apellido = _apellido
        self.edad = _edad

    """ Declaración de funciones de la instancia de la clase """
    def estudiarMateria(self, _materia, _horas):
        print(f"Estoy estudiando {_materia} durante {_horas} horas")
