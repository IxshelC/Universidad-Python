class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # Método calular Area  (base*altura)
    def area(self):
        return self.base * self.altura

# Objetos
Area1=Rectangulo(base= (float(input("Proporcione la base: "))),altura=(float(input("Proporcione la altura: "))))
print(f'El área es: {Area1.area()}')


Area2=Rectangulo(base= (float(input("Proporcione la base: "))),altura=(float(input("Proporcione la altura: "))))
print(f'El área es: {Area2.area()}')