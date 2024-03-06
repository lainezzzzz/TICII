Diego Linares Ortiz

### Para el error de "Dime quien eres"
```bash:
git config --global user.email "tucorreo@g.educaand.es"
git config --global user.name "tuNombre"
```

### Subir vuestro código al repositorio
```bash:
git add .
git commit -m "Cambios de tuNombre"
git pull
git push
```

### "Descargar" los cambios de vuestr@s compañer@s
```bash:
git pull
```

### Consejos para los ejercicios

#### Ejer1

1. Declarar una variable de tipo lista
```Python:
lista_alojamientos = []
```
2. Abrir el fichero
```Python:
fichero = open("ruta del fichero")
```
3. Una vez abierto el fichero, LEEMOS el fichero
```Python:
lineas_todos_datos = fichero.readLines()
```
4. Recorrer la lista de todos los datos (estamos recorriendo todas las líneas leídas del fichero)
```Python:
for linea in lineas_todos_datos:
```
5. La primera línea no tiene datos, sólo es la línea de cabecera
6. La segunda línea ya empieza a contener los datos.
    - Separar los datos por comas
    ```Python:
    datos_separados_por_lineas = linea.split(",")
    ```
    - Crear un diccionario de datos para contener la información que pide el enunciado
    ```Python:
    TODO
    ```
### Datos de prueba para que probéis vuestros ejercicios

```Python:
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
```
    

