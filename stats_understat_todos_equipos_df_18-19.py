"""Importación de librerías necesarias"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

path = "C:/Users/lolo9/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)
website1 = "https://understat.com/league/"
website2 = "https://understat.com/team/"


lista_ligas = ["La_liga","EPL","Bundesliga","Serie_A","Ligue_1"]
lista_anos = ["2019","2018"]
lista_header_formation = ["Nº", "Formation", "Min", "Sh", "G", "ShA", "GA", "xG", "xGA", "xGD", "xG90", "xGA90", "Año", "Club"]
lista_equipo = []           #Almacena los equipos de una clasificacion
lista_equipos = []          #Almacena los equipos de todas las clasificaciones
lista_formation = []        #Almacena los datos de una formacion
lista_formations = []       #Almacena los datos de todas las foramciones de un equipo

for x in lista_ligas:
    for y in lista_anos:
        url = website1 + "/" + x + "/" + y      #url de las clasificaciones de las ligas
        #print(url)
        driver.get(url)
        time.sleep(2)   #Retardo
        rows = driver.find_elements(By.XPATH, '//*[@id="league-chemp"]/table/tbody/tr')
        for z in range(1,len(rows)+1):       #Recorre todas las filas de la tabla por separado
            driver.get(url)
            dato = driver.find_element(By.XPATH, "//*[@id='league-chemp']/table/tbody/tr["+str(z)+"]/td[2]").text  #Selecciona el elemento 2 de cada fila, el equipo
            if " " in dato:
                dato = dato.replace(" ","_")    #Dato en el formato para crear la url correctamente
            lista_equipo.append(dato)
            print(dato)
            url2 = website2 + dato + "/" + y    #url de las stats de los equipos
            #print(url2)
            driver.get(url2)
            time.sleep(2)
            formation_boton = driver.find_element(By.XPATH,'//label[@for="statistic-2"]')
            formation_boton.click()
            rows_formation = driver.find_elements(By.XPATH, '//*[@id="team-statistics"]/table/tbody/tr')
            for k in range(1,len(rows_formation)+1):       #Recorre todas las filas de la tabla por separado
                for h in range(1,13):
                    lista_formation.append(driver.find_element(By.XPATH, "//*[@id='team-statistics']/table/tbody/tr["+str(k)+"]/td["+str(h)+"]").text)
                lista_formation.append(y)   #Añadimos el año a la fila
                lista_formation.append(dato)    #Añadimos el club a la fila
                #lista_formation.append(x)
                lista_formations.append(lista_formation)
                lista_formation = []    #Borramos la lista para volver a almacenar las stats de otra formacion
            #print(lista_formations)            
        lista_equipos.append(lista_equipo)
        #print(lista_equipo)
        lista_equipo = []   #Borramos la lista para volver a almacenar los equipos de otra clasificacion

"""Creación del dataframe"""
df = pd.DataFrame(lista_formations, columns = lista_header_formation)
print(df)
df.to_csv('Stats_Understat_18_19.csv',index=False)