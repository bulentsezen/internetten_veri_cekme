from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import pandas as pd

driver_path = "D:\Selenium\chromedriver.exe"
browser = webdriver.Chrome(driver_path)

browser.get("https://www.science.org/journal/scirobotics/research")
#time.sleep(1)

kaynak = browser.page_source
soup = BeautifulSoup(kaynak, "html.parser")

metinler = soup.find_all("div",attrs={"class":"d-flex justify-content-between align-items-end"})

liste = []

for metin in metinler:
    baslik = metin.find("span", attrs={"class": "hlFld-Title"}).text
    liste.append([baslik])

sonraki_sayfa_butonu = soup.find("li", attrs={"class":"page-item__arrow--next page-item"})

for a in sonraki_sayfa_butonu.find_all('a', href=True):
    sonraki_sayfa_linki = a['href']
    print(sonraki_sayfa_linki)

p = 0

while p < 14:
    browser.get(sonraki_sayfa_linki)
    kaynak = browser.page_source
    soup = BeautifulSoup(kaynak, "html.parser")

    metinler = soup.find_all("div", attrs={"class": "d-flex justify-content-between align-items-end"})

    for metin in metinler:
        baslik = metin.find("span", attrs={"class": "hlFld-Title"}).text
        liste.append([baslik])

    sonraki_sayfa_butonu = soup.find("li", attrs={"class": "page-item__arrow--next page-item"})

    for a in sonraki_sayfa_butonu.find_all('a', href=True):
        sonraki_sayfa_linki = a['href']
        print(sonraki_sayfa_linki)

    p = p + 1




veritabani = pd.DataFrame(liste)           # install pandas
veritabani.columns=["Makale Başlıkları"]
veritabani.to_excel("makaleler.xlsx")       # install openpyxl
