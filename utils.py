import pandas as pd

EXCEL_PATH = "data/capbudg.xlsx"

def get_table_names():
    try:
        xls = pd.ExcelFile(EXCEL_PATH)
        return xls.sheet_names
    except Exception as e:
        return []

def get_row_names(sheet_name):
    try:
        df = pd.read_excel(EXCEL_PATH, sheet_name=sheet_name)
        return df.iloc[:, 0].dropna().astype(str).tolist()
    except Exception as e:
        return []

def sum_row_values(sheet_name, row_name):
    try:
        df = pd.read_excel(EXCEL_PATH, sheet_name=sheet_name)
        row = df[df.iloc[:, 0].astype(str) == row_name]
        if row.empty:
            return 0
        numeric_data = pd.to_numeric(row.iloc[0, 1:], errors='coerce')
        return numeric_data.sum(skipna=True)
    except Exception as e:
        return 0
