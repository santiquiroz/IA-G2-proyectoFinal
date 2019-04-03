# IA-G2-proyectoFinal
Miembros del equipo:
	Santiago Quiroz Upegui (squirozu@unal.edu.co)
	Mirai Alejandro Kaneko ()
	el negro...
Notas:
1. El intervalo de agrupamiento de los datos esta dado por defecto en 5 segundos.
2. El intervalo de obtencion de datos esta dado por defecto en 4 dias para los datos de entrenamiento y 4 horas para los datos de evaluacion.
3. Los datos de entrenamiento son tomados desde 2019-03-20 12:00:00 hasta 2019-03-24 12:00:00.
4. Los datos de evaluacion son tomados desde 4 horas antes de la ejecucion del la obtencion de estos.
Instrucciones de Instalacion y operacion:
1. Descomprimir el proyecto
2. Instalas las siguientes librerias con pip:
    - elasticsearch
    - pandas
    - json
    - xlswriter
    - openpyxl
    - numpy
3. Ejecutar main.py
4. Con la opción 3 obtener los datos de entrenamiento y evaluación
5. Con la opción 4 abrir las opciones de etiquetado:
    - Con la opción 3 etiquetar todos los datos
6. Salir con opción 5

7. Abrir Weka
8. Abrir package manager de Weka:
9. Buscar e instalar los siguientes paquetes:
    - wekaExcel
    - wekaODF
10. Cerrar package manager
11. Abrir explorer en Weka
12. Dar click en el botón "Open File"
13. En la carpeta de entrenamiento seleccionar "trainingSINDATOS-ETIQUETADOS.xlsx"
14. Dar click en "classify"     
15. Dar clock en "choose"
16. Seleccionar en "trees", "J48"
17. En "test options" seleccionar "use training set"
18. Seleccionar clase "ETIQUETADO"
19. Click en "Start"
20. Click derecho sobre el arbol y guardar el modelo (save model)
21. Cerrar el explorer
22. Abrir el explorer
23. Click en "Open File"
24. En la carpeta de evaluacion seleccionar "evauluationSINDATOS-ETIQUETADOS.xlsx"
25. Click en "Save"
26. Guardar como arff
27. Click en la pestaña "classify"
28. En "test options" seleccionar "supplied set"
29. Click en el botón "set"
30. Abrir el archivo arff
31. Cambiar clase a ETIQUETADO y cerrar
32. Click en "more options"
33. En "output predictions" dar click en "choose"
34. Seleccionar Plain Text
35. Click en "ok"
36. Bajo test options cambiar la clase a ETIQUETADO
37. Click derecho en el recuadro vacío
38. Dar click en "Load model"
39. Seleccionar el modelo guardado
40. Click derecho en el modelo cargado
41. Dar click en "Re-evaluate model on current test set"	

