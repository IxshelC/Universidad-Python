# Crear clase
class Persona:

    def __init__(self,nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarDetalle(self):
        print(f'Persona:{self.nombre} {self.apellido} {self.edad}')


Persona1 = Persona("Ixshel","Corona",26)
Persona1.mostrarDetalle()

Persona2 = Persona("Carlos","Martinez", 40)
Persona2.mostrarDetalle()