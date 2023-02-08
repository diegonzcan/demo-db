#### Librerias
import requests
from bs4 import BeautifulSoup
import pandas as pd

#### Constantes

uni_dur = []
precios = []
masters = []
tipo = []

#### Variables

path = """C:\\Users\\diego\\OneDrive\\Documents\\SEMINAT_SCRAPE\\"""
headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}


#### Formulas

def SeminatScrape():
    print("Scraping Seminat...")
    for i in range(1,245):
        r = requests.get(f"https://www.seminat.net/programas?goto=true&page={i}#programs", headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        tarjeta = soup.find_all('p', attrs={'class':'small mt-1'})
        print(f"Scraping page {i}")
        for i in tarjeta:
            uni_dur.append(i.text.strip())
            precio_ = i.find_next('p')
            precios.append(precio_.text.strip())
            
        for i in soup.find_all('div', attrs = {"class":"card-body-programs"}):
            maestria = i.find('p')
            type = i.find('h3')
            masters.append(maestria)
            tipo.append(type)
    print("Complete!")
    df = pd.DataFrame({
            "Programa":masters,
            "Duracion/Universidad":uni_dur,
            "Precio":precios,
            "Tipo":tipo
        })
    return df

def saveToCsv(df):
    df.to_csv(path  + "seminat.csv",encoding = 'utf-8-sig', index=False)

#### RUN!

if __name__ == '__main__':
    saveToCsv(SeminatScrape())
