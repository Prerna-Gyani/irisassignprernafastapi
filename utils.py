import pandas as pd

EXCEL_PATH = "data/capbudg.xlsx"

def get_table_names():
    try:
        xls = pd.ExcelFile(EXCEL_PATH)
        return xls.sheet_names
    except:
        return []

def get_row_names(sheet):
    try:
        df = pd.read_excel(EXCEL_PATH, sheet_name=sheet)
        return df.iloc[:, 0].dropna().astype(str).tolist()
    except:
        return []

def sum_row_values(sheet, row_name):
    df = pd.read_excel(EXCEL_PATH, sheet_name=sheet)
    row = df[df.iloc[:, 0].astype(str) == row_name]
    if row.empty:
        return 0
    numeric_data = row.iloc[0, 1:].apply(pd.to_numeric, errors='coerce')
    return numeric_data.sum(skipna=True)
