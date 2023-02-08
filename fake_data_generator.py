from faker import Faker
from faker.providers import internet
import pandas as pd
import random
import datetime
from datetime import date
import sqlConnect as s
import pandas as pd

cursor = s.cnxn.cursor()
archivo = f"{datetime.datetime.now().strftime('%Y_%m_%d')}_sales_dly.csv"
local_path = """C:\\Users\\diego\\OneDrive\\Documents\\SEMINAT_SCRAPE\\daily_sales_csvs\\"""


def main():
    
    global df 
    
    local_path = """C:\\Users\\diego\\OneDrive\\Documents\\SEMINAT_SCRAPE\\daily_sales_csvs\\"""

    catalog = pd.read_csv('seminat_clean.csv')

    fake = Faker('es_MX')

    l1,l2,l3,l4,l5,l6,l7,l8,l9 = [],[],[],[],[],[],[],[],[]

    daily_ventas = random.randint(1,30)
    for i in range(daily_ventas):
        asesor = random.randint(6,11)
        profile = fake.profile()
        variable = random.randint(0,3890)
        programa_ID = variable
        precio = catalog.Precio[variable]
        alumno = profile['name']
        beca = random.randint(10,60) / 100
        sexo = profile['sex']
        address = fake.address()
        banco = fake.bank()
        date_time = fake.date_between(date.today(), date.today())
        l1.append(programa_ID)
        l2.append(precio)
        l3.append(alumno)
        l4.append(beca)
        l5.append(sexo)
        l6.append(address)
        l7.append(banco)
        l8.append(date_time)
        l9.append(asesor)
        df = pd.DataFrame({
            'program_id': l1,
            'id_asesor': l9,
            'precio': l2,
            'alumno': l3,
            'beca': l4,
            'sexo': l5,
            'direccion':l6,
            'banco':l7,
            'fecha':l8
        })    
    print(f'El dia de hoy se vendieron {len(df)} programas')

    archivo = f"{datetime.datetime.now().strftime('%Y_%m_%d')}_sales_dly.csv"
    df.to_csv(local_path + archivo, encoding='utf-8-sig')
    print(f"Se ha guardado exitosamente el archivo {archivo}")

def load():
    print("loading data...")
    for index, row in df.iterrows():
        cursor.execute('''INSERT INTO venta_hist(
            id_programa, id_asesor, precio, alumno, beca, sexo, direccion, banco, fecha) VALUES (?,?,?,?,?,?,?,?,?)''', 
        row.program_id,row.id_asesor,row.precio,row.alumno,row.beca, row.sexo, row.direccion, row.banco, row.fecha)
    print(f"{df.shape[0]} rows succesfully loaded into SQL Server")
    s.cnxn.commit()
    cursor.close()



if __name__ == "__main__":
    main()
    load()