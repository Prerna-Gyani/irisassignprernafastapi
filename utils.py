import pandas as pd
import os

DATA_DIR = "data"

def get_excel_sheets():
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".xlsx")]
    return files

def read_sheet(file_name):
    file_path = os.path.join(DATA_DIR, file_name)
    return pd.read_excel(file_path, sheet_name=None, header=None)

def get_table_names(file_name):
    return list(read_sheet(file_name).keys())

def get_table_data(file_name, table_name):
    sheets = read_sheet(file_name)
    return sheets[table_name]

def get_row_names(file_name, table_name):
    df = get_table_data(file_name, table_name)
    return df.iloc[:, 0].dropna().tolist()

def get_row_sum(file_name, table_name, row_name):
    df = get_table_data(file_name, table_name)
    row = df[df.iloc[:, 0] == row_name]
    if row.empty:
        return None
    numeric_values = pd.to_numeric(row.iloc[0, 1:], errors='coerce')
    return numeric_values.dropna().sum()
