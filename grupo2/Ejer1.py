def extraer_del_fichero_ejer1():
    """
    Extraer del fichero de alojamientos una lista con todos los alojamientos, 
    donde cada alojamiento sea un diccionario que contenga el identificador del alojamiento, 
    el identificador del anfitrión, el distrito y el precio
    
    Ejemplo:
    Fichero
    id,name,host_id,host_name,neighbourhood_group,neighbourhood,latitude,longitude,room_type,price,minimum_nights,number_of_reviews,last_review,reviews_per_month,calculated_host_listings_count,availability_365,number_of_reviews_ltm,license
    561654306981369438,Vacation home in Sevilla · ★4.69 · 1 bedroom · 2 beds · 1 bath,209748933,Mariano,Triana,Triana Oeste,37.3891716003418,-6.009562015533447,Entire home/apt,281,1,16,2023-11-13,0.78,44,87,9,VFT/SE/04999
    15479525,Home in Sevilla · ★4.63 · 2 bedrooms · 7 beds · 3 baths,99370256,Mi Casa,Casco Antiguo,Alfalfa,37.38967,-5.99562,Entire home/apt,484,2,119,2023-12-03,1.36,5,288,15,VFT/SE/00873

    0º Declarar una variable (una lista) que va a contener la información que debéis almacenar, es decir, la información que os pide el enunciado
    1º Abrir el fichero
    2º Leer el fichero
    3º Recorrer todas las lineas del fichero
    4º 
    La primera línea contiene: id,name,host_id,host_name,neighbourhood_group,neighbourhood,latitude,longitude,room_type,price,minimum_nights,number_of_reviews,last_review,reviews_per_month,calculated_host_listings_count,availability_365,number_of_reviews_ltm,license
    La segunda línea contendrá: 561654306981369438,Vacation home in Sevilla · ★4.69 · 1 bedroom · 2 beds · 1 bath,209748933,Mariano,Triana,Triana Oeste,37.3891716003418,-6.009562015533447,Entire home/apt,281,1,16,2023-11-13,0.78,44,87,9,VFT/SE/04999
    La tercera línea contendrá: 15479525,Home in Sevilla · ★4.63 · 2 bedrooms · 7 beds · 3 baths,99370256,Mi Casa,Casco Antiguo,Alfalfa,37.38967,-5.99562,Entire home/apt,484,2,119,2023-12-03,1.36,5,288,15,VFT/SE/00873
    Y así sucesivamente
    5º Hay que obtener, el identificador del alojamiento, el identificador del anfitrión, el distrito y el precio
    6º Crear un diccionario con esa información, y añadir este diccionario a la lista creada en el paso 0.
    7º Cuando hayáis recorrido todas las líneas, fuera del bucle, cerráis el archivo y devolvéis la lista creada en el paso 0 de la siguiente manera:
    return nombre_lista
    """

    alojamientos = []  
    
    with open('sevilla.csv', 'r') as archivo: 
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

