import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")
st.title("IRIS Excel Processor Assignment – Streamlit Version")

# Load Excel file
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

# Extract Table Names based on the expected section titles in the first column
def extract_table_names(df):
    # Expected sections in the first column
    expected_tables = ["INITIAL INVESTMENT", "WORKING CAPITAL", "GROWTH RATES", "SALVAGE VALUE", "OPERATING CASHFLOWS", "EBITDA", "EBIT", "NATCF"]
    table_names = []

    for i, row in df.iterrows():
        if isinstance(row[0], str) and row[0].strip().upper() in expected_tables:
            table_names.append(row[0].strip())
    
    return table_names

# Extract the table names
table_names = extract_table_names(df)

# Add a sidebar for navigation options
option = st.sidebar.selectbox(
    "Select an Option",
    ["List Tables (/list_tables)", "Get Table Details (/get_table_details)", "Row Sum (/row_sum)"]
)

# 1. List Tables
if option == "List Tables (/list_tables)":
    st.subheader("Available Tables in Excel File")
    st.json({"tables": table_names})

# 2. Get Table Details
elif option == "Get Table Details (/get_table_details)":
    # Table selection from the extracted table names
    table = st.selectbox("Select Table", table_names)
    
    # Display content of selected table
    st.subheader(f"Details for {table}")
    
    # Finding the starting row for the selected table
    start_row = df[df.iloc[:, 0].str.contains(table, case=False, na=False)].index[0]
    end_row = start_row + 10  # Show next 10 rows of that table section
    st.write(f"Displaying rows from {start_row} to {end_row}")
    
    # Display a few rows after that start row
    st.write(df.iloc[start_row:end_row])  # Adjust to show more or fewer rows based on content

# 3. Row Sum
elif option == "Row Sum (/row_sum)":
    table = st.selectbox("Select Table", table_names)
    row_name = st.text_input("Enter Row Name", "")

    # Search for the row_name in the selected table
    row_data = df[df.iloc[:, 0].str.contains(row_name, case=False, na=False)]
    if not row_data.empty:
        values = row_data.iloc[0, 1:].values  # Extracting values excluding the first column
        total = sum([val for val in values if isinstance(val, (int, float))])
        st.json({"table_name": table, "row_name": row_name, "sum": total})
    else:
        st.error("Row not found.")
