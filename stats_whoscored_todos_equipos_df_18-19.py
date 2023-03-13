"""Importación de librerías necesarias"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

path = "C:/Users/lolo9/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)

lista_website = ["https://es.whoscored.com/Regions/206/Tournaments/4/Seasons/7889/Stages/17702/TeamStatistics/Espa%C3%B1a-LaLiga-2019-2020",
                "https://es.whoscored.com/Regions/206/Tournaments/4/Seasons/7466/Stages/16546/TeamStatistics/Espa%C3%B1a-LaLiga-2018-2019",
                "https://es.whoscored.com/Regions/252/Tournaments/2/Seasons/7811/Stages/17590/TeamStatistics/Inglaterra-Premier-League-2019-2020",
                "https://es.whoscored.com/Regions/252/Tournaments/2/Seasons/7361/Stages/16368/TeamStatistics/Inglaterra-Premier-League-2018-2019",
                "https://es.whoscored.com/Regions/81/Tournaments/3/Seasons/7872/Stages/17682/TeamStatistics/Alemania-Bundesliga-2019-2020",
                "https://es.whoscored.com/Regions/81/Tournaments/3/Seasons/7405/Stages/16427/TeamStatistics/Alemania-Bundesliga-2018-2019",
                "https://es.whoscored.com/Regions/108/Tournaments/5/Seasons/7928/Stages/17835/TeamStatistics/Italia-Serie-A-2019-2020",
                "https://es.whoscored.com/Regions/108/Tournaments/5/Seasons/7468/Stages/16548/TeamStatistics/Italia-Serie-A-2018-2019",
                "https://es.whoscored.com/Regions/74/Tournaments/22/Seasons/7814/Stages/17593/TeamStatistics/Francia-Ligue-1-2019-2020",
                "https://es.whoscored.com/Regions/74/Tournaments/22/Seasons/7344/Stages/16348/TeamStatistics/Francia-Ligue-1-2018-2019",
                ]


lista_header_whoscored = ["Club","Goles","Tiros pp","Amarillas","Rojas","Posesión (%)","Acierto Pase (%)","Aéreos","Rating","Año","Pais"]
lista_whoscored = []            #Almacena las stats de cada equipo
lista_whoscoreds = []           #Almacena las stats de todos los equipos de la clasificacion


"""driver.get("https://es.whoscored.com/Regions/252/Tournaments/2/Seasons/8228/Stages/18685/TeamStatistics/Inglaterra-Premier-League-2020-2021")
time.sleep(2)

rows = driver.find_elements(By.XPATH, "//*[@id='top-team-stats-summary-content']/tr")
for f in range(0,len(rows)):       #Muestra por pantalla todas las filas de la tabla por separado
    print(rows[f].text)"""

for url in lista_website:
    print(url)
    driver.get(url)
    time.sleep(2)   
    rows_whoscored = driver.find_elements(By.XPATH, "//*[@id='top-team-stats-summary-content']/tr")
    for k in range(1,len(rows_whoscored)+1):        #Recorre todas las filas de la tabla por separado
        for h in range(1,len(lista_header_whoscored)-2):
            if h == 4:                              #Las 'amarillas' y las 'rojas' vienen en la misma celda. De esta forma, las separamos
                amarillas = driver.find_element(By.XPATH,"//*[@id='top-team-stats-summary-content']/tr["+str(k)+"]/td[4]/span[1]")
                lista_whoscored.append(amarillas.text)
                rojas = driver.find_element(By.XPATH,"//*[@id='top-team-stats-summary-content']/tr["+str(k)+"]/td[4]/span[2]")
                lista_whoscored.append(rojas.text)
            else:
                lista_whoscored.append(driver.find_element(By.XPATH, "//*[@id='top-team-stats-summary-content']/tr["+str(k)+"]/td["+str(h)+"]").text)
        lista_whoscored.append(url[-9:-5])            #Extracción del año
        i = lista_website[lista_website.index(url)].rfind("/")
        ii = lista_website[lista_website.index(url)].find("-",i,len(lista_website[lista_website.index(url)]))
        lista_whoscored.append(lista_website[lista_website.index(url)][i+1:ii])
        lista_whoscoreds.append(lista_whoscored)
        lista_whoscored = []                        #Borramos la lista para volver a almacenar las stats de otra formacion

"""Creación del dataframe"""
df = pd.DataFrame(lista_whoscoreds, columns = lista_header_whoscored)
print(df)
df.to_csv('Stats_WhoScored_18_19.csv',index=False)