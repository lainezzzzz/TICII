def alojamientos_de_anfitriones(lista_alojamientos):
    """
Crear una función que reciba la lista de alojamientos y muestre los anfitriones y el número de alojamientos que posee cada uno.    """

    anfitriones = {}
    
    for alojamiento in lista_alojamientos:
        anfitrión = alojamiento['anfitrión']
        
        if anfitrión in anfitriones:
            anfitriones[anfitrión] += 1
        else:
            anfitriones[anfitrión] = 1
    
    for anfitrión, cantidad in anfitriones.items():
        print(f"{anfitrión}: {cantidad} alojamientos")