# Crear clase
class Persona:

    def __init__(self,nombre, apellido, edad,*valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrarDetalle(self):
        print(f'Persona:{self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')


Persona1 = Persona("Ixshel","Corona",26, 'Quetzalli', 557895122, m='Mango', f='Fresa')
Persona1.mostrarDetalle()

Persona2 = Persona("Carlos","Martinez", 40)
Persona2.mostrarDetalle()