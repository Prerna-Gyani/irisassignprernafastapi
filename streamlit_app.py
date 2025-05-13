import streamlit as st
import pandas as pd
import os
import re

st.set_page_config(layout="wide")
st.title("IRIS Excel Processor Assignment – Streamlit Version")

# Function to load the Excel file
@st.cache_data
def load_excel(file):
    return pd.read_excel(file, sheet_name=None)

# Path to the Excel file
file_path = "data/capbudg.xls"
if not os.path.exists(file_path):
    st.error("Missing capbudg.xls in /data folder.")
    st.stop()

# Load the Excel file and extract sheet names
sheets = load_excel(file_path)
sheet_name = "CapBudgWS"
df = sheets[sheet_name]

# Debugging: Show sheet content
st.write(f"Sheet Content Loaded: {df.head()}")

# Function to detect table boundaries based on the content
def extract_table_names(df):
    # This is an example where we identify rows that start with capitalized headings
    table_names = []
    for i, row in df.iterrows():
        # If the first column is a section header, treat it as a table name
        if isinstance(row[0], str) and row[0].isupper() and not row[0].startswith(' '):
            table_names.append(row[0].strip())
    return table_names

# Extract the table names based on the structure of the Excel sheet
table_names = extract_table_names(df)

# 1. List Tables
if option == "List Tables (/list_tables)":
    st.subheader("Available Tables in Excel File")
    st.json({"tables": table_names})

# 2. Get Table Details
elif option == "Get Table Details (/get_table_details)":
    # Table selection from the extracted table names
    table = st.selectbox("Select Table", table_names)
    
    # Find the rows for the selected table
    rows = []
    for i, row in df.iterrows():
        if isinstance(row[0], str) and row[0].strip().startswith(table):
            rows.append(row[0].strip())
    
    st.json({"table_name": table, "row_names": rows})

# 3. Row Sum
elif option == "Row Sum (/row_sum)":
    table = st.selectbox("Select Table", table_names)
    row_name = st.text_input("Enter Row Name", "")

    # Search for the row_name in the selected table
    row_data = df[df.iloc[:, 0].str.contains(row_name, case=False, na=False)]
    if not row_data.empty:
        values = row_data.iloc[0, 1:].values
        total = sum([val for val in values if isinstance(val, (int, float))])
        st.json({"table_name": table, "row_name": row_name, "sum": total})
    else:
        st.error("Row not found.")
