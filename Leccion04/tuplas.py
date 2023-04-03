# Definir una tupla
frutas = ("Mango","Piña", "Fresa")
print(frutas)

# Saber el largo
print(len(frutas))

# Acceder a un elemento
print(frutas[0])

# Navegación inversa
print(frutas[-1])

# Acceder a un rango
print(frutas[0:2]) # No incluye el último valor

# Recorrer elementos
for fruta in frutas:
    print(fruta, end =' ')

# Cambiar el valor de tupla
frutasLista = list(frutas)
frutasLista[0] = "Melón"
frutas = tuple(frutasLista)
print("\n", frutas)