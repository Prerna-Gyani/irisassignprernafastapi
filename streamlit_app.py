import streamlit as st
from utils import get_excel_sheets, get_table_names, get_table_data, get_row_names, get_row_sum

st.title("IRIS Excel Processor Prerna Gyanchandani Assignment")
st.subheader("Process and analyze Excel data interactively.")

selected_file = st.selectbox("Select a table (sheet):", get_excel_sheets())

if selected_file:
    table_names = get_table_names(selected_file)
    selected_table = st.selectbox("Select a worksheet:", table_names)

    if selected_table:
        st.subheader("Table Data")
        df = get_table_data(selected_file, selected_table)
        st.dataframe(df)

        st.subheader("Select a row to calculate sum:")
        row_names = get_row_names(selected_file, selected_table)
        selected_row = st.selectbox("Row name:", row_names)

        if selected_row:
            row_sum = get_row_sum(selected_file, selected_table, selected_row)
            st.success(f"Sum of values in row '{selected_row}' is: {row_sum}")
