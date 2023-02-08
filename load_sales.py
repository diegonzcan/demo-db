import sqlConnect as s
import pandas as pd
import fake_data_generator as f

df = pd.read_csv(f'{f.local_path}' + f'{f.archivo}')

cursor = s.cnxn.cursor()

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
    load()