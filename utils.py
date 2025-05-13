import pandas as pd

EXCEL_PATH = "data/capbudg.xlsx"

def get_table_names():
    try:
        return pd.ExcelFile(EXCEL_PATH).sheet_names
    except FileNotFoundError:
        return []

def get_row_names(sheet_name):
    df = pd.read_excel(EXCEL_PATH, sheet_name=sheet_name)
    # first column, drop blanks
    return df.iloc[:, 0].dropna().astype(str).tolist()

def sum_row_values(sheet_name, row_name):
    df = pd.read_excel(EXCEL_PATH, sheet_name=sheet_name)
    # locate the row
    row = df[df.iloc[:, 0].astype(str) == row_name]
    if row.empty:
        return 0
    # sum all numeric columns (skip the first one)
    nums = pd.to_numeric(row.iloc[0, 1:], errors="coerce")
    return nums.sum(skipna=True)
