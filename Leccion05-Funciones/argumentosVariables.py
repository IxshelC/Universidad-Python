def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(Nombre='Carlos')
listarTerminos( Nombre='Jimena')

