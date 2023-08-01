# Creando clase Aritmetica

class Aritmetica:
    """
    Clase Aritmética para realizar las operaciones de SUmar, restar, etc
    """

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    # Método de sumar
    def sumar(self):
        return self.numero1 + self.numero2

    # Método de restar
    def restar(self):
        return self.numero1 - self.numero2

    # Método multiplciar
    def multiplicar(self):
        return self.numero1 * self.numero2

    # Método Dividir
    def divisor(self):
        return self.numero1 / self.numero2



# Objeto 1
Aritmetica1 =   Aritmetica(2,3)
print(f'Suma: {Aritmetica1.sumar()}')

#Objeto 2
Aritmetica2 = Aritmetica(5,3)
print(f'Resta: {Aritmetica2.restar()}')

# Objeto 3
Aritmetica3 = Aritmetica(5,2)
print(f'Multiplicar: {Aritmetica3.multiplicar()}')

# Objeto 4
Aritmetica4 = Aritmetica(10,2)
print(f'Dividir: {Aritmetica4.divisor()}')
