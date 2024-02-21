def extraer_del_fichero_ejer1():
    """
    Extraer del fichero de alojamientos una lista con todos los alojamientos, 
    donde cada alojamiento sea un diccionario que contenga el identificador del alojamiento, 
    el identificador del anfitrión, el distrito y el precio.
    
    Ejemplo:
    Fichero
    id,name,host_id,host_name,neighbourhood_group,neighbourhood,latitude,longitude,room_type,price,minimum_nights,number_of_reviews,last_review,reviews_per_month,calculated_host_listings_count,availability_365,number_of_reviews_ltm,license
    96033,Rental unit in Málaga · ★4.62 · 2 bedrooms · 2 beds · 1 bath,510467,Rafael,,Este,36.72031,-4.35627,Entire home/apt,53,3,206,2023-12-17,1.66,1,260,43,VFT/MA/22043
    166473,Rental unit in Málaga · ★4.73 · 1 bedroom · 4 beds · 2 shared baths,793360,Fred,,Este,36.72031,-4.36108,Private room,19,5,94,2023-11-04,0.63,4,189,6,

    0º Declarar una variable (una lista) que va a contener la información que debéis almacenar, es decir, la información que os pide el enunciado
    1º Abrir el fichero
    2º Leer el fichero
    3º Recorrer todas las lineas del fichero
    4º 
    La primera línea contiene: id,name,host_id,host_name,neighbourhood_group,neighbourhood,latitude,longitude,room_type,price,minimum_nights,number_of_reviews,last_review,reviews_per_month,calculated_host_listings_count,availability_365,number_of_reviews_ltm,license
    La segunda línea contendrá: 96033,Rental unit in Málaga · ★4.62 · 2 bedrooms · 2 beds · 1 bath,510467,Rafael,,Este,36.72031,-4.35627,Entire home/apt,53,3,206,2023-12-17,1.66,1,260,43,VFT/MA/22043
    La tercera línea contendrá: 166473,Rental unit in Málaga · ★4.73 · 1 bedroom · 4 beds · 2 shared baths,793360,Fred,,Este,36.72031,-4.36108,Private room,19,5,94,2023-11-04,0.63,4,189,6,
    Y así sucesivamente
    5º Hay que obtener, el identificador del alojamiento, el identificador del anfitrión, el distrito y el precio
    6º Crear un diccionario con esa información, y añadir este diccionario a la lista creada en el paso 0.
    7º Cuando hayáis recorrido todas las líneas, fuera del bucle, cerráis el archivo y devolvéis la lista creada en el paso 0 de la siguiente manera:
    return nombre_lista
    """
    