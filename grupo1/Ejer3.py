def alojamientos_para_viajeros(lista_alojamientos):
    """
    Crear una función que reciba la lista de alojamientos, pregunte por el presupuesto y 
    muestre la lista de alojamientos que se ajusten al presupuesto dado.
    """
    lista_alojamientos = [
        {'nombre': 'Hotel A', 'precio': 100},
        {'nombre': 'Hotel B', 'precio': 150},
        {'nombre': 'Hotel C', 'precio': 200},
        {'nombre': 'Hotel D', 'precio': 250}
    ]

    presupuesto = float(input("Ingrese su presupuesto: "))

    alojamientos_compatibles = []
    for alojamiento in lista_alojamientos:
        if alojamiento['precio'] <= presupuesto:
            alojamientos_compatibles.append(alojamiento)
    
    if alojamientos_compatibles:
        print("Los alojamientos que se adapta a su presuouesto son:")
        for alojamiento in alojamientos_compatibles:
            print("- Nombre:", alojamiento['nombre'],
                  "| Precio:", alojamiento['precio'])
    
    return alojamientos_compatibles