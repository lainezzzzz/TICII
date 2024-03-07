#def alojamientos_para_viajeros(lista_alojamientos):
"""
Crear una función que reciba la lista de alojamientos, pregunte por el presupuesto y 
muestre la lista de alojamientos que se ajusten al presupuesto dado.
"""
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


presupuesto = float(input("Ingrese su presupuesto: "))

alojamientos_compatibles = []
for alojamiento in lista_alojamientos:
    if float (alojamiento[("price")]) <= presupuesto:
        alojamientos_compatibles.append(alojamiento)

if alojamientos_compatibles:
    print("Los alojamientos que se adapta a su presuouesto son:")
    for alojamiento in alojamientos_compatibles:
        print("- Nombre:", alojamiento['host_id'],
                "| Precio:", alojamiento['price'])

#return alojamientos_compatibles