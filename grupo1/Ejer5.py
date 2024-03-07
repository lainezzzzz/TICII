# def alojamientos_de_anfitriones(lista_alojamientos):

    # Crear una función que reciba la lista de alojamientos y muestre los anfitriones y el número de alojamientos que posee cada uno.

lista_alojamientos = [
        {"id":"96033",
        "host_id":"510467",
        "neighbourhood":"Este",
        "price":"53"},
        {"id":"96035",
        "host_id":"5540467",
        "neighbourhood":"Centro",
        "price":"70"},
        {"id":"987654",
        "host_id":"65432",
        "neighbourhood":"Este",
        "price":"25"},
        {"id":"1234",
        "host_id":"4567",
        "neighbourhood":"Este",
        "price":"93"},
        {"id":"86408",
        "host_id":"789",
        "neighbourhood":"Centro",
        "price":"60"},
        {"id":"844",
        "host_id":"8712315",
        "neighbourhood":"Este",
        "price":"40"}
        ]


    # Recorrer la lista. Cada posición de la lista es un diccionario
    # Para cada diccionario, accedes a host_id... ese host_id lo añades a un diccionario propio
    # AL recorrer la lista, cuentas cuántas veces aparece ese host id
    # Guardas cuántas veces aparece y lo almacenas en el diccionario que has creado antes

alojamiento_anfitriones = {}

for alojamiento in lista_alojamientos:
    if alojamiento['host_id'] in alojamiento_anfitriones.keys():
        alojamiento_anfitriones[alojamiento['host_id']] += 1
    else:
        alojamiento_anfitriones[alojamiento['host_id']] = 1

print(alojamiento_anfitriones)