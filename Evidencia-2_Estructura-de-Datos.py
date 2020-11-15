import pandas as pd
import datetime
import csv
import sys
import os.path

separador = ("-" * 60) + "\n"
ciclo = 1
opcion =1
num_ventas = 0

if os.path.exists("Productos.csv") == True:
    productos = pd.read_csv("Productos.csv", index_col=0)
else:
   prod_dict = {'Nombre':['Pulsera','Aretes','Cadena','Anillo','Cuff'],
                 'Precio':[60,80,40,60,50],
                 'Descripcion':['Dijes Intercambiables','Colgantes Largos','Dije de Mariposa','Con Glitter','Strass']}
   productos = pd.DataFrame(prod_dict)
    
if os.path.exists("Ventas.csv") == True:
    ventas = pd.read_csv("Ventas.csv", index_col=0)
else:
    ventas = pd.DataFrame(columns=["Fecha", "Hora", "ID producto", "Cantidad", "Pago total"])

print ("\t Bisuteria y Joyeria S.A de C.V.")
print (separador)

print ("*MENU DE INTERACCION USUARIO* \n")


while ciclo == 1:

    print("¿Que desea hacer? \n")
    print("1. Registrar una venta")
    print("2. Consultar ventas en un dia especifico")
    print("3. Salir")
    print()

    opcion = int(input("**Ingrese el numero de opcion** \n"))
    print (separador)

    if opcion == 1:
        precio_total = 0
        
        while opcion == 1:
            print(productos['Nombre'])
            print(separador)
            
            id_venta = int(input("ID del objeto \n>"))
            cant_venta = int(input("Cantidad a vender \n>"))
            opcion = int(input("Agregar otro producto? 1.Si 2.No \n>"))
            precio_total += productos.iloc[id_venta,1] * cant_venta
            print(" ")
            
        fecha_hora = datetime.datetime.now().replace(microsecond=0)
        solo_fecha = fecha_hora.date()
        solo_hora = fecha_hora.time()
        
        ventas = ventas.append({'Fecha':solo_fecha.strftime('%d/%m/%y'), 'Hora':solo_hora.strftime('%H:%M:%S'), 'ID producto':id_venta, 'Cantidad':cant_venta, 'Pago total':precio_total}, ignore_index=True)
        print(f'Precio total a pagar: {precio_total}')
        print(separador)

    elif opcion == 2:
        fecha_capt = input("Que fecha quiere ver?, Ejemplo '13/11/20' dd/mm/aa \n>") 
        
        for i in ventas.index:
            if fecha_capt == ventas.loc[i,'Fecha']:
                print(ventas.iloc[i])
                print(separador)
                num_ventas += 1
            else:
                pass
                
        if num_ventas == 0:
            print("No se ah encontrado ninguna venta en esa fecha")
        num_ventas = 0
        print(separador)

    elif opcion == 3:
        try:
            productos.to_csv(r'Productos.csv', index=True, header=True)
        except Exception:
            print(f"Ocurrió un problema {sys.exc_info()[0]}")
        else:
            print("Datos de productos guardados exitosamente")
        
        try:
            ventas.to_csv('Ventas.csv', index=True, header=True)
        except Exception:
            print(f"Ocurrió un problema {sys.exc_info()[0]}")
        else:
            print("Datos de ventas guardados exitosamente")
        finally:
            ciclo = 0
            print ("Programa concluido :)")
    
    else:
        print("Numero equivocado")
        print(separador)
   
        
        
        
        
        