def alojamientos_para_viajeros(lista_alojamientos):
    """
    Crear una función que reciba la lista de alojamientos, pregunte por el presupuesto y 
    muestre la lista de alojamientos que se ajusten al presupuesto dado.
    """
    lista_alojamientos = [
        {'id': "736863",'host_id': "287276", 'neighbourhood': "Este", 'price': 100},
        {'id': "734796",'host_id': "7492642", 'neighbourhood': "Centro", 'price': 150},
        {'id': "8362468",'host_id': "635424", 'neighbourhood': "Churriana", 'price': 200},
        {'id': "2837628",'host_id': "276345", 'neighbourhood': "Carretera de Cadiz", 'price': 250}
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