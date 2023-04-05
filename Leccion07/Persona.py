
"""
    El Objetivo del encapsulamiento es que no podamos acceder directamente a los atributos de nuestra clase.

    Método GET -> Obtienen / recupear los atributos
    Método SET -> Modificar / colocar los atributos de nuestra clase
"""
class Persona:

    def __init__(self,nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Decorador permite que podamos acceder al atributo
    @property
    def nombre(self):
        print('Llamando método get nombre')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print('Llamando método set nombre')
        self._nombre = nombre

    def mostrarDetalle(self):
        print(f'Persona:{self._nombre} {self.apellido} {self.edad} ')


Persona1 = Persona("Ixshel","Corona",26)
Persona1.nombre = 'Ixi Crown'
print(Persona1.nombre)

