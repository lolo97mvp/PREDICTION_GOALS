"""Importación de librerías necesarias"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

path = "C:/Users/lolo9/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)

#driver.get("https://www.transfermarkt.es/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2020")
#time.sleep(3)
#rows_transfermarkt = driver.find_elements(By.XPATH, "//*[@id='yw1']/table/tbody/tr")
#print(rows_transfermarkt.text)
#for f in range(0,len(rows_transfermarkt)):       #Muestra por pantalla todas las filas de la tabla por separado
#    print(rows_transfermarkt[f].text,"aaa")

lista_website = ["https://www.transfermarkt.es/laliga/startseite/wettbewerb/ES1/plus/?saison_id=",
                  "https://www.transfermarkt.es/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=",
                  "https://www.transfermarkt.es/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=",
                  "https://www.transfermarkt.es/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=",
                  "https://www.transfermarkt.es/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id="]
lista_anos = ["2018","2019"]
lista_header_transfermarkt = ["Club","Nº jugadores","Edad","Extranjeros","Media valor mercado","Valor de mercado","Año","Liga"]
lista_transfermarkt = []                #Almacena las stats de cada equipo
lista_transfermarkts = []               #Almacena las stats de todos los equipos de la clasificacion

for a in lista_website:
    for b in lista_anos:
        url = a + b
        print(url)
        driver.get(url)
        time.sleep(5)
        rows_transfermarkt = driver.find_elements(By.XPATH, "//*[@id='yw1']/table/tbody/tr")
        for k in range(1,len(rows_transfermarkt)+1):       #Muestra por pantalla todas las filas de la tabla por separado
            for h in range(2,len(lista_header_transfermarkt)):
                lista_transfermarkt.append(driver.find_element(By.XPATH, "//*[@id='yw1']/table/tbody/tr["+str(k)+"]/td["+str(h)+"]").text)
            lista_transfermarkt.append(b)
            i = lista_website[lista_website.index(a)].find(".es/")
            ii = lista_website[lista_website.index(a)].find("/startseite",i,len(lista_website[lista_website.index(a)]))
            lista_transfermarkt.append(lista_website[lista_website.index(a)][i+4:ii])
            lista_transfermarkts.append(lista_transfermarkt)
            lista_transfermarkt = []    #Borramos la lista para volver a almacenar las stats de otro equipo

#Creación del dataframe
df = pd.DataFrame(lista_transfermarkts, columns = lista_header_transfermarkt)
print(df)
df.to_csv('Stats_Transfermarktt_18_19.csv',index=False)