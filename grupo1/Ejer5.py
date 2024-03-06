# def alojamientos_de_anfitriones(lista_alojamientos):
    # """
    # Crear una función que reciba la lista de alojamientos y muestre los anfitriones y el número de alojamientos que posee cada uno.
    # """
lista_alojamientos = [{"id":"96033",
        "host_id":"510467",
        "neighbourhood":"Este",
        "price":"53"},{"id":"96034",
        "host_id":"510468",
        "neighbourhood":"Este",
        "price":"20"},{"id":"96038",
        "host_id":"510467",
        "neighbourhood":"Este",
        "price":"80"} ]


    # Recorrer la lista. Cada posición de la lista es un diccionario
    # Para cada diccionario, accedes a host_id... ese host_id lo añades a un diccionario propio
    # AL recorrer la lista, cuentas cuántas veces aparece ese host id
    # Guardas cuántas veces aparece y lo almacenas en el diccionario que has creado antes

alojamiento_anfitriones = {}
    # Recorremos la lista de alojamientos
for alojamiento in lista_alojamientos:
        # Si el anfitrión ya aparece como clave del diccionario, incrementamos su valor en uno
    if alojamiento['host_id'] in alojamiento_anfitriones.keys():
        alojamiento_anfitriones[alojamiento['host_id']] += 1
        # Si el anfitrión no aparece como clave del diccionario, lo añadimos con valor 1.
    else:
        alojamiento_anfitriones[alojamiento['host_id']] = 1

print(alojamiento_anfitriones)