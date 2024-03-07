def n_alojamientos_por_distrito_ejer2(lista_alojamientos):
    """
    Crear una función que reciba la lista de alojamientos y muestre el número de alojamientos en cada distrito.
    
    Parámetros:
    - lista_alojamientos: lista de diccionarios.
    
    Ejemplo:
    
    lista_alojamientos = [
        {"id":"96033",
        "host_id":"510467",
        "neighbourhood":"Este",
        "price":"53"}
        ]
    
    
    """
    
    lista_alojamientos = [
        {"id":"96033",
        "host_id":"510467",
        "neighbourhood":"Este",
        "price":"53"},
        {"id":"250154",
        "host_id":"346238",
        "neighbourhood":"Norte",
        "price":"75"},
        {"id":"459858",
        "host_id":"298567",
        "neighbourhood":"Oeste",
        "price":"110"},
        {"id":"649210",
        "host_id":"187453",
        "neighbourhood":"Centro",
        "price":"65"}
    ]

    for alojamientos in lista_alojamientos:
        print:(alojamientos["datos"])
 