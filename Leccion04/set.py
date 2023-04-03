# set ( no guarda orden)
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

# Largo
print(len(planetas))

# Revisar si un elemento está presente
print("Tierra" in planetas)

# Agregar un elemento
planetas.add("Tierra")
print(planetas)

#Eliminar un elemento
planetas.remove("Tierra")
print(planetas)
planetas.discard('Tierra')
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar el set
del planetas
print(planetas)