import requests
from bs4 import BeautifulSoup
import pandas as pd

#### Functions 
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

lista = [i for i in range(245)]

def getSeq():
    s = chunks(lista, 10)
    for l in s:
        print(l)

#### END FUNCTIONS

path = """C:\\Users\\diego\\OneDrive\\Documents\\SEMINAT_SCRAPE\\"""

headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

descripciones = []
def extractDesc():
    print("Scraping Seminat")
    s = chunks(lista, 10)
    for l in s:
        for i in l:          
            print(f'Scraping page {i}')
            r = requests.get(f'https://www.seminat.net/programas?goto=true&page={i}#programs',  headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            tarjeta = soup.find_all('div', attrs={'class':'col-lg-3 col-sm-6'})
            for i in tarjeta:
                link = i.find_next('a', href=True)
                link = (link['href'])
                r = requests.get(link, headers=headers)
                soup = BeautifulSoup(r.content, 'html.parser')
                card = soup.find_all('div', attrs= {'class':'card-description-program-detail'})
                for i in card:
                    desc = i.find('p')
                    descripciones.append(desc.text.strip())
        df = pd.DataFrame({'descripcion':descripciones})
        df.to_csv(path  + "descriptions.csv",encoding = 'utf-8-sig', index=False)
        return df

if __name__ == '__main__':
    extractDesc()

### correr loop completo
### error handling de productos sin desc
### auto_incremental sql load