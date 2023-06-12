from entity import Alumno, AlumnoEspecial

""" Creacion de objetos """
alumno = Alumno("Lucas","Zarandon", 23)
alumno1 = Alumno("Luciano","Esperlazza", 25)

alumno2 = AlumnoEspecial("Lionel","Messi", 35)

""" Llamado a atributos y metodos """
print(alumno.nombre) 
alumno.presentarse()
alumno.estudiar()
alumno.estudiarMateria("Python")

alumno1.presentarse()
alumno1.estudiarMateria("Java")

alumno2.presentarse()
alumno2.estudiar()
alumno2.estudiarMateria("Python",8)