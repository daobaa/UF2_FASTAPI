import insert_data_csv_to_db as insert_data
import pandas as pd
import os

def csv_to_json():
    csv_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'paraules_tematica_penjat.csv'))
    if os.path.exists(csv_file_path):
        df = pd.read_csv(csv_file_path)
        d = df.to_dict(orient='list')
        return d
    else:
        print(f"El archivo no se encuentra en la ruta: {csv_file_path}")
        return None

data = csv_to_json()

for i in range(500):
    insert_data.insert_data_csv_to_db(i, data)