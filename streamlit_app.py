import streamlit as st
from utils import get_table_names, get_row_names, sum_row_values

st.set_page_config(page_title="IRIS Prerna Gyanchandani Assignment")

st.title("IRIS Prerna Gyanchandani Assignment")
st.markdown("#### Excel: capbudg.xlsx")

# 1️⃣ List all sheets
tables = get_table_names()
if not tables:
    st.error("No sheets found in data/capbudg.xlsx")
    st.stop()

table = st.selectbox("Select a table", tables)

# 2️⃣ Show row names (first-column values)
if table:
    rows = get_row_names(table)
    st.subheader("Row Names in “%s”" % table)
    st.write(rows)

    # 3️⃣ Pick a row and calculate its numeric sum
    row_choice = st.selectbox("Select a row to sum its numeric values", rows)
    if st.button("Calculate Sum"):
        total = sum_row_values(table, row_choice)
        st.success(f"Sum of numeric values in “{row_choice}”: **{total}**")
