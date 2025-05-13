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
sheet_names = list(sheets.keys())  # Extract the sheet names

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
    # Manually list tables based on your Excel sheet structure
    # Adjust these names to reflect the correct sections in your sheet
    table_names = [
        "Initial Investment",
        "Cashflow Details",
        "Discount Rate",
        "Working Capital",
        "Growth Rates",
        "Investment Measures",
        "Book Value & Depreciation"
    ]
    st.json({"tables": table_names})

# 2. Get Table Details
elif option == "Get Table Details (/get_table_details)":
    # Table selection from the manually specified list
    table = st.selectbox("Select Table", [
        "Initial Investment",
        "Cashflow Details",
        "Discount Rate",
        "Working Capital",
        "Growth Rates",
        "Investment Measures",
        "Book Value & Depreciation"
    ])
    
    df = sheets["Sheet1"]  # Assuming data is in the first sheet
    row_names = []  # Placeholder for row names
    
    # Example logic for handling the "Initial Investment" table:
    if table == "Initial Investment":
        row_names = [
            "Initial Investment=",
            "Opportunity cost (if any)=",
            "Lifetime of the investment",
            "Salvage Value at end of project=",
            "Deprec. method(1:St.line;2:DDB)=",
            "Tax Credit (if any )=",
            "Other invest.(non-depreciable)="
        ]
    elif table == "Working Capital":
        row_names = [
            "Initial Investment in Work. Cap=",
            "Working Capital as % of Rev=",
            "Salvageable fraction at end="
        ]
    
    # Displaying row names
    st.json({"table_name": table, "row_names": row_names})

# 3. Row Sum
elif option == "Row Sum (/row_sum)":
    # Table selection from the manually specified list
    table = st.selectbox("Select Table", [
        "Initial Investment",
        "Cashflow Details",
        "Discount Rate",
        "Working Capital",
        "Growth Rates",
        "Investment Measures",
        "Book Value & Depreciation"
    ])
    
    df = sheets["Sheet1"]  # Assuming data is in the first sheet

    if table == "Initial Investment":
        row_names = [
            "Initial Investment=",
            "Opportunity cost (if any)=",
            "Lifetime of the investment",
            "Salvage Value at end of project=",
            "Deprec. method(1:St.line;2:DDB)=",
            "Tax Credit (if any )=",
            "Other invest.(non-depreciable)="
        ]
    # Add logic for other tables

    # Row selection and sum calculation
    row_name = st.selectbox("Select Row", row_names)
    row_index = df[df.iloc[:, 0].astype(str) == row_name].index

    if not row_index.empty:
        values = df.iloc[row_index[0], 1:]
        total = 0
        for v in values:
            if isinstance(v, (int, float)):
                total += v
            elif isinstance(v, str):
                # Match numbers in the string
                matches = re.findall(r"[-+]?\d*\.\d+|\d+", v)
                total += sum(float(x) for x in matches)
        st.json({"table_name": table, "row_name": row_name, "sum": total})
    else:
        st.error("Row not found.")
