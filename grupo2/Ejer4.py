def alojamiento_mas_barato(lista_alojamientos):

distrito = input("Ingrese su ubicacion favorita  donde desee gastar dinero: ")

alojamientos_en_distrito = [alojamiento for alojamiento in lista_alojamientos if alojamiento['distrito'] == distrito]

if not alojamientos_en_distrito:
    print("Lo siento, no eh podido encontrar nada en esta ubicación.")
    return

alojamiento_mas_barato = min(alojamientos_en_distrito, key=lambda x: x['precio'])

print("El alojamiento más barato en tu ubicación deseada", distrito, "es:")
print("Su nombre es:", alojamiento_mas_barato['nombre'])
print("Tiene un precio de:", alojamiento_mas_barato['precio'])
print("Esta dentro del tipo de alojamiento:", alojamiento_mas_barato['tipo'])
