import streamlit as st
from utils import get_table_names, get_row_names, sum_row_values

st.set_page_config(page_title="IRIS Prerna Gyanchandani Assignment")

st.title("IRIS Prerna Gyanchandani Assignment")
st.markdown("### Excel Sheet: capbudg.xlsx")

tables = get_table_names()

if not tables:
    st.warning("No tables found in the Excel file.")
else:
    table = st.selectbox("Select a table", tables)

    if table:
        row_names = get_row_names(table)
        st.subheader("Row Names")
        st.write(row_names)

        row = st.selectbox("Select a row to calculate sum", row_names)
        if st.button("Calculate Sum"):
            total = sum_row_values(table, row)
            st.success(f"Sum of numeric values in row: {total}")
