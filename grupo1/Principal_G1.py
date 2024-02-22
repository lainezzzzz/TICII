import Ejer1 as ejer1
import Ejer2 as ejer2
import Ejer3 as ejer3
import Ejer4 as ejer4
import Ejer5 as ejer5

def principal():
    
    # Extraemos los datos del fichero
    #lista_alojamientos = ejer1.extraer_del_fichero_ejer1()
    lista_alojamientos = [1,2,3]
    opc = 0
    
    while(opc != 5):
        print("1. Mostrar alojamientos por distrito")
        print("2. Mostrar alojamientos por presupuesto")
        print("3. Mostrar alojamiento más barato del distrito")
        print("4. Mostrar anfitriones y alojamientos")
        print("5. Salir")
        
        opc = int(input("Introduzca la opcion deseada"))
        
        if opc == 1:
            ejer2.n_alojamientos_por_distrito_ejer2(lista_alojamientos)
        elif opc == 2:
            ejer3.alojamientos_para_viajeros(lista_alojamientos)
        elif opc == 3:
            ejer4.alojamiento_mas_barato(lista_alojamientos)
        elif opc == 4:
            ejer5.alojamientos_de_anfitriones(lista_alojamientos=lista_alojamientos)
        elif opc == 5:
            print("Saliendo...")
        else:
            print("Opcion no soportada")

if __name__ == "__main__":
    principal()
    
    
    