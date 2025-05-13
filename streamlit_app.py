import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")
st.title("IRIS Excel Processor Assignment – Streamlit Version")

@st.cache_data
def load_excel(file):
    return pd.read_excel(file, sheet_name=None)

# Load file
file_path = "data/capbudg.xls"
if not os.path.exists(file_path):
    st.error("Missing capbudg.xls in /data folder.")
    st.stop()

# Load the Excel file and extract sheet names
sheets = load_excel(file_path)
sheet_names = list(sheets.keys())  # This should give the correct sheet names

# Debugging: Show sheet names
st.write(f"Sheet Names Extracted: {sheet_names}")

option = st.sidebar.selectbox("Choose Functionality", [
    "List Tables (/list_tables)",
    "Get Table Details (/get_table_details)",
    "Row Sum (/row_sum)"
])

# 1. List Tables
if option == "List Tables (/list_tables)":
    st.subheader("Available Tables in Excel File")
    st.json({"tables": sheet_names})

# 2. Get Table Details
elif option == "Get Table Details (/get_table_details)":
    table = st.selectbox("Select Table", sheet_names)
    df = sheets[table]
    if not df.empty:
        row_names = df.iloc[:, 0].dropna().astype(str).tolist()
        st.json({"table_name": table, "row_names": row_names})
    else:
        st.warning("Selected table is empty.")

# 3. Row Sum
elif option == "Row Sum (/row_sum)":
    table = st.selectbox("Select Table", sheet_names)
    df = sheets[table]

    if not df.empty:
        row_names = df.iloc[:, 0].dropna().astype(str).tolist()
        row = st.selectbox("Select Row", row_names)
        row_index = df[df.iloc[:, 0].astype(str) == row].index

        if not row_index.empty:
            values = df.iloc[row_index[0], 1:]
            total = 0
            for v in values:
                if isinstance(v, (int, float)):
                    total += v
                elif isinstance(v, str):
                    matches = re.findall(r"[-+]?\d*\.\d+|\d+", v)
                    total += sum(float(x) for x in matches)
            st.json({"table_name": table, "row_name": row, "sum": total})
        else:
            st.error("Row not found.")
    else:
        st.warning("Selected table is empty.")
