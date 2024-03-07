

#def alojamiento_mas_barato(lista_alojamientos):
"""
Crear una función que reciba la lista de alojamientos, pregunte al usuario por un distrito, y muestre el alojamiento más barato del distrito.
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

distrito = input("Ingrese su ubicacion favorita donde desee gastar dinero: ")

id_mas_barato=""
precio_mas_barato = 10000
for distrito in lista_alojamientos:
# Declara una variable para almacenar el id más barato
# Declara una variable para almacenar el precio más barato... la igualas a 10000
# 1º recorre la lista_alojamientos
# 2º Comparas el precio de ese elemento con el precio mas barato
# Si el precio es más barato, entonces, la variable precio_mas_barato es el precio de ese elemento
# También, almacenas el id del elemento en tu variable id_mas_barato


# Muestras por pantalla ambas variables


if not alojamientos_en_distrito:
    print("Lo siento, no eh podido encontrar nada en esta ubicación.")
    #return

print("El alojamiento más barato en tu ubicación deseada", distrito, "es:")
#print("Su nombre es:", alojamiento_mas_barato['nombre'])
#print("Tiene un precio de:", alojamiento_mas_barato['precio'])
#print("Esta dentro del tipo de alojamiento:", alojamiento_mas_barato['tipo'])


