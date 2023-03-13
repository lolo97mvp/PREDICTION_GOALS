# PREDICTION_GOALS
 El objetivo de este proyecto es intentar extraer conclusiones, buscar relación entre distintas estadísticas e intentar predecir el número de goles marcados por los equipos durante esta temporada. Para ello, se han recopilado estadísticas de todos los equipos de las cinco grandes ligas europeas (España, Inglaterra, Alemania, Italia y Francia) desde la temporada 2018/19 hasta la actual.

Descripción de los archivos que forman el proyecto:

· Los archivos de python con el siguiente nombre stats_/nombre web/ son los scripts
  que extraen la información de las webs. Solo se incluye los de la 18/19 y 19/20 ya que
  el código para las temporadas restantes es el mismo. Se dividió así debido a que el
  tiempo de ejecución del código era demasiado.

· Los archivos 'csv' son los datasets con las estadísticas ya extraidas. Por un lado están
  los de la 18/19 y 19/20 y los de la 20/21, 21/22 y 22/23 por otro.

· El archivo 'data_clean_' es el script donde se realiza la limpieza y la preparación de los datos.

· El archivo 'part-00000-adc783a0-6f62-4ffe-bc1a-b167eb5b4ec3-c000.csv' es el generado por
  PySpark tras realizar la limpieza y la preparación de los datos.

· El archivo 'data_ML_all_18-22' es el script donde se realiza el análisis de los datos y
  los modelos de Machine Learning.
