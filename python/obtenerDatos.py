from elasticsearch import Elasticsearch
from elasticsearch import helpers
#import pandas as pd
import json
import csv
"""autor: Santiago Quiroz Upegui (squiroz@unal.edu.co)
"""

#los guardados los pensaba hacer con hilos pero ya no hay tiempo para programar
numeroTurnos=0
colaDeGuardado = 0


def formatearDatos():
    print("Proceso de formadeado a JSON inicializado.")
    datos=[""]
    with open("./Datos crudos/Originales/datos.json", "r") as f:
        datos = f.read()
        datos=datos.replace("}\n][","},")
        print(datos)
        with open("./Datos crudos/Formateados/datos.json", "w") as data_file:
            data_file.write(datos)
    f.close()
    data_file.close()
    print("Datos formateados a formato valido JSON con exito.")
    return True


#guarda los datos[un arreglo de hits(json)] en un json (cada fragmento esta detro de un [] (corregir luego llamando a formatear datos)"
def guardarTXT(datos,turno,totaldatos):
    global colaDeGuardado
    global numeroTurnos
    print("numero de entradas en fragmeto: "+str(len(datos)))
    print("Cola: "+str(colaDeGuardado))
    print("Turno: "+str(numeroTurnos))
    while True:
        
        if colaDeGuardado == turno:
            print("proceso de guardado "+str(turno)+" inicializado")
            break
        else:
            print("proceso de guardado "+str(turno)+" esperando")

    
    
    print("proceso de guardado: "+str(turno))

    
    
    #guardando en disco
    with open("./Datos crudos/Originales/datos.json", "a") as data_file:
        json.dump(datos, data_file, indent=2)
    print("numero de entradas guardadas con exito: "+str(totaldatos))
    clasificar(datos,turno,totaldatos)
    return True


#guarda los datos[un arreglo de hits(json)] en un csv segun el tipo de json
def clasificar():
    return True

#obtiene los datos de la base de datos y los guarda
def get(es,tamanoLectura,tamanoBase):
    global colaDeGuardado
    global numeroTurnos
    contador = 0
    totaldatos = 0
    resultados = [None]*tamanoLectura
    res = helpers.scan(es,index="test-index",query={"query":{"match_all":{}}})
    print("Obtencion de base inicializada.")
    for hit in res:
        if contador == 0:
            print("Lectura de fragmento inicializada.")
            
        if ((hit != None)and(totaldatos != tamanoBase)):
            
            if contador == tamanoLectura:
                #guardando la parte
                print("Lectura de fragmento finalizada.")
                guardarTXT(resultados,numeroTurnos,totaldatos)
                numeroTurnos=numeroTurnos+1
                resultados = [None]*tamanoLectura
                
                contador = 0
            else:
                resultados[contador] = hit            
                
                contador=contador + 1
                totaldatos = totaldatos + 1
        else:
            razon = "se ha llegado al final de la base de datos. Razon: "
            if hit == None:
                razon = razon+"no hay mas datos que leer. "
                #guardando la parte
                guardarTXT(resultados[:contador],numeroTurnos,totaldatos)
                numeroTurnos=numeroTurnos+1
                resultados = [None]*tamanoLectura
            if (totaldatos) == tamanoBase:
                razon = razon+"se ha llegado al limite de datos preestablecido. "
                #guardando la parte
                guardarTXT(resultados[:contador],numeroTurnos,totaldatos)
                numeroTurnos=numeroTurnos+1
                resultados = [None]*tamanoLectura
            contador=0
            print(razon)
            break
        
    return True
        
if __name__ == "__main__":
    es = Elasticsearch(['54.147.121.162'],
    #http_auth=('user', 'secret'),
    scheme="http",
    port=9200,
    timeout=30)

    print("ingrese el numero de la accion deseada: ")
    print("1.Obtener datos del servidor.")
    print("2.Formatear datos originales a un json correcto.")
    print("3.obtener csv")
    eleccion = int(input("opcion:"))
    if eleccion == 1:
                print("NOTA:por lo general una entrada equivale a 1kb")
                #numero de entradas que se quiere leer a la vez del servidor
                tamanoLectura = int(input("Ingrese numero de entradas por iteracion: "))
                

                #tamano maximo de la base de datos deseada
                tamanoBase = int(input("Ingrese el total de entradas que se recuperaran: "))

                get(es,tamanoLectura,tamanoBase)

                formatearDatos()
    elif eleccion == 2:
        formatearDatos()
    elif eleccion == 3:
        clasificar()
    else:
        print("me quiero morir")
        
    
    
    
        #break
        
        
        #print(json.dumps(hit)+"\n")
            
       

