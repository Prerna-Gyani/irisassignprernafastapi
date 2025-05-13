import os
import pandas as pd

DATA_FOLDER = "data"

def get_table_names():
    return [f for f in os.listdir(DATA_FOLDER) if f.endswith(".xlsx")]

def get_table_data(table_name):
    path = os.path.join(DATA_FOLDER, table_name)
    if not os.path.exists(path):
        raise ValueError("Table not found")
    df = pd.read_excel(path)
    return df

def add_row_to_table(table_name, row_dict):
    path = os.path.join(DATA_FOLDER, table_name)
    df = pd.read_excel(path)
    df = pd.concat([df, pd.DataFrame([row_dict])], ignore_index=True)
    df.to_excel(path, index=False)

def delete_row_from_table(table_name, row_index):
    path = os.path.join(DATA_FOLDER, table_name)
    df = pd.read_excel(path)
    if row_index < 0 or row_index >= len(df):
        raise IndexError("Invalid row index")
    df = df.drop(index=row_index).reset_index(drop=True)
    df.to_excel(path, index=False)
