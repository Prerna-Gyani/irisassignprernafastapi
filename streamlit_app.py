import streamlit as st
from utils import get_table_names, get_row_names, sum_row_values

st.set_page_config(page_title="IRIS Excel Processor Assignment")

st.title("IRIS Excel Processor Prerna Gyanchandani Assignment")
st.markdown("Process and analyze Excel data interactively.")

# Step 1: List all tables (sheet names)
tables = get_table_names()
if not tables:
    st.error("No tables found in the Excel file.")
    st.stop()

selected_table = st.selectbox("Select a table (sheet):", tables)

# Step 2: Display row names for the selected table
row_names = get_row_names(selected_table)
if not row_names:
    st.warning("No rows found in the selected table.")
    st.stop()

selected_row = st.selectbox("Select a row to calculate sum:", row_names)

# Step 3: Calculate sum of numeric values in the selected row
if st.button("Calculate Sum"):
    total = sum_row_values(selected_table, selected_row)
    st.success(f"Sum of numeric values in '{selected_row}': {total}")
