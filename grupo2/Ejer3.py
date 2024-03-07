    """
    Crear una función que reciba la lista de alojamientos, pregunte por el presupuesto y 
    muestre la lista de alojamientos que se ajusten al presupuesto dado.
    """
    

def filtrar_por_presupuesto(alojamientos, presupuesto):
    alojamientos_compatibles = []

    for alojamiento in alojamientos:
        if float(alojamiento.get("price")) <= presupuesto:
            alojamientos_compatibles.append(alojamiento)

    return alojamientos_compatibles

# Datos de prueba 
lista_alojamientos = [
    {"id": "96033", "host_id": "510467", "neighbourhood": "Este", "price": "53"},
    {"id": "96035", "host_id": "5540467", "neighbourhood": "Centro", "price": "70"},
    {"id": "987654", "host_id": "65432", "neighbourhood": "Este", "price": "25"},
    {"id": "1234", "host_id": "4567", "neighbourhood": "Este", "price": "93"},
    {"id": "86408", "host_id": "789", "neighbourhood": "Centro", "price": "60"},
    {"id": "844", "host_id": "8712315", "neighbourhood": "Este", "price": "40"}
]

#float hace que a a la hora de poner el input para poner el presuspuesto pueda usar numeros con decimales
presupuesto_usuario = float(input("Ingrese su presupuesto: "))

resultados = filtrar_por_presupuesto(lista_alojamientos, presupuesto_usuario)

if resultados:
    print("Alojamientos compatibles con su presupuesto:")
    for alojamiento in resultados:
        print(f"ID: {alojamiento['id']} - Precio: {alojamiento['price']}")
else:
    print("Lo siento, no hay alojamientos disponibles dentro de su presupuesto.")