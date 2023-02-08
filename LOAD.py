import sqlConnect as s
import pandas as pd

df = pd.read_csv('seminat_clean.csv')

cursor = s.cnxn.cursor()

print("loading data...")
for index, row in df.iterrows():
    cursor.execute('''INSERT INTO programas(Programas, Universidad, Duracion, Precio, Tipo, Moneda) VALUES (?,?,?,?,?,?)''', row.Programa,row.Universidad,row.Duracion,row.Precio,row.Tipo, row.Moneda)
print(f"{df.shape[0]} rows succesfully loaded into SQL Server")
s.cnxn.commit()
cursor.close()


