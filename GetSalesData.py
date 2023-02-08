from faker import Faker
from faker.providers import internet
import pandas as pd
import random

catalog = pd.read_csv('seminat_clean.csv')

fake = Faker()


l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
daily_ventas = random.randint(1,30)
for i in range(daily_ventas):
    profile = fake.profile()
    variable = random.randint(0,3890)
    programa_ID = variable
    precio = catalog.Precio[variable]
    alumno = profile['name']
    beca = random.randint(10,60) / 100
    sexo = profile['sex']
    l1.append(programa_ID)
    l2.append(precio)
    l3.append(alumno)
    l4.append(beca)
    l5.append(sexo)
    df = pd.DataFrame({
        'program_id': l1,
        'precio': l2,
        'alumno': l3,
        'beca': l4,
        'sexo': l5
    })    
print(f'El dia de hoy se vendieron {len(df)} programas')
print(df)