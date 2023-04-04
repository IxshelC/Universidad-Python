# Clase cubo

class cubo:
    #Atributos (ancho, alto,profundidad)
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    # Método Calcular Volumen Ancho*profundo*Alto
    def volumen(self):
        return self.ancho*self.profundidad*self.alto

# Objetos
volumen = cubo(ancho =(float(input('Ingresa el ancho:'))), alto=(float(input('Ingresa el alto: '))), profundidad = float(input('Ingresa la profundidad: ')) )
print(f'Volumen cubo: {volumen.volumen()}')

