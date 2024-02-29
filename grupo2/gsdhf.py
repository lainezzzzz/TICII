
    alojamientos = []  
    
    with open('nombre_del_fichero.csv', 'r') as archivo: 
        next(archivo)  
        for linea in archivo:  
            datos = linea.strip().split(',') 
            identificador = datos[0]
            id_anfitrion = datos[2]
            distrito = datos[5]
            precio = int(datos[9])
            alojamiento = {
                'id': identificador,
                'host_id': id_anfitrion,
                'distrito': distrito,
                'precio': precio
            }
            alojamientos.append(alojamiento)
    
    return alojamientos  