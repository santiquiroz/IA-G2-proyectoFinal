from elasticsearch import Elasticsearch
from elasticsearch import helpers
import pandas as pd
import json as json
import csv
import xlsxwriter


from datetime import datetime, date, time, timedelta
import calendar

"""autor: Santiago Quiroz Upegui (squiroz@unal.edu.co)
"""
#obtiene los datos en un intervalo de tiempo y los guarda en un arreglo 
def getInterval(es,inferior, superior):
    

    print("Obteniendo datos con scan")
    
    cres = helpers.scan(es,index="test-index", query={"query": {
    "bool": {
      "must": [
        {
          "match_all": {}
        },
        {
          "range": {
            "dt": {
              "gte": inferior.strftime('%Y-%m-%d %H:%M:%S'),
              "lte": superior.strftime('%Y-%m-%d %H:%M:%S'),
              "format": "yyyy-MM-dd HH:mm:ss||epoch_millis"
            }
          }
        }
      ],
      "filter": [],
      "should": [],
      "must_not": []
    }}},preserve_order=True)
    crestresults=[]
    for hit in cres:
        crestresults.append(hit)
    
    print(len(crestresults))
    return crestresults
#obtiene arreglos de intervalos de tiempo, cuenta cuantos datos hay en cada intervalo y los guarda en disco segun la ruta dada
def getTotal(es,inferior,fechaFinal,intervaloSegundos,directorio):
    intervalo=[]
    cantidad=[]
    datos=[]
    superior=datetime.now()
    while inferior < fechaFinal:
        #print("inferior: "+inferior.strftime('%Y-%m-%d %H:%M:%S'))
        superior =inferior + timedelta(seconds=intervaloSegundos)
        if superior > fechaFinal :
            superior = fechaFinal
        #print("superior: "+superior.strftime('%Y-%m-%d %H:%M:%S'))
        result=getInterval(es,inferior,superior)
        intervalo.append((inferior.strftime('%Y-%m-%d %H:%M:%S')+'//'+superior.strftime('%Y-%m-%d %H:%M:%S')))
        cantidad.append(len(result))
        datos.append([result])
        inferior=superior
    
    #escribiendo en disco
    
    entradas=len(cantidad)
    #df = pd.DataFrame({'Intervalo': intervalo,'VEIzquierda':[None]*entradas,'VEDerecha':[None]*entradas,'Etiquetado':[None]*entradas,'Cantidad': cantidad,'Datos':datos})
    df = pd.DataFrame({'Intervalo': intervalo,'Etiquetado':[None]*entradas,'Cantidad': cantidad,'Datos':datos})
    print(df)
    print("Guardando en disco.")
    writer = pd.ExcelWriter(directorio+".xlsx", engine='xlsxwriter')
    df.to_excel(writer,index_label = 'indice', sheet_name='hoja1')
    writer.save()
    df = pd.DataFrame({'Intervalo': intervalo,'Etiquetado':[None]*entradas,'Cantidad': cantidad})
    writer = pd.ExcelWriter(directorio+"SINDATOS.xlsx", engine='xlsxwriter')
    df.to_excel(writer,index_label = 'indice', sheet_name='hoja1')
    writer.save()
    return True
def getTrainingData(es,intervaloSegundos = 5):
    directorio = "./Entrenamiento/training"
    fechaInicial= datetime.strptime('2019-03-24 11:00:00', '%Y-%m-%d %H:%M:%S')
    fechaFinal= datetime.strptime('2019-03-24 12:00:00', '%Y-%m-%d %H:%M:%S')
    print("inicial: "+fechaInicial.strftime('%Y-%m-%d %H:%M:%S'))
    print("final: "+fechaFinal.strftime('%Y-%m-%d %H:%M:%S'))
    getTotal(es,fechaInicial,fechaFinal,intervaloSegundos,directorio)
    return True
    
def getActualData(es,intervaloSegundos = 5):
    directorio = "./Evaluacion/evaluation"
    fechaFinal= datetime.now()
    fechaInicial= fechaFinal-timedelta(hours=1)
    print("inicial: "+fechaInicial.strftime('%Y-%m-%d %H:%M:%S'))
    print("final: "+fechaFinal.strftime('%Y-%m-%d %H:%M:%S'))
    getTotal(es,fechaInicial,fechaFinal,intervaloSegundos,directorio)
    
    return True

if __name__ == "__main__":
    es = Elasticsearch(['54.147.121.162'],
    #http_auth=('user', 'secret'), 
    scheme="http",
    port=9200,
    timeout=30)
    opcion= int(input("Ingrese 1 para obtener datos de entrenamiento o otro nuemero para evaluacion."))
    if opcion == 1:
        getTrainingData(es)
    else:
        getActualData(es)
         
