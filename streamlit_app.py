import streamlit as st
from utils import get_table_names, get_table_data, add_row_to_table, delete_row_from_table

st.title("IRIS Prerna Gyanchandani Assignment ")

# --- Choose table ---
tables = get_table_names()
table_choice = st.selectbox("Select a table", tables)

if table_choice:
    df = get_table_data(table_choice)
    st.subheader("Table Data")
    st.dataframe(df)

    # --- Add Row ---
    st.subheader("Add Row")
    row_data = {}
    for col in df.columns:
        row_data[col] = st.text_input(f"Enter value for '{col}'", key=col)
    
    if st.button("Add Row"):
        try:
            add_row_to_table(table_choice, row_data)
            st.success("Row added successfully. Refresh the page to see the update.")
        except Exception as e:
            st.error(f"Error: {e}")

    # --- Delete Row ---
    st.subheader("Delete Row")
    delete_index = st.number_input("Enter row index to delete", min_value=0, max_value=len(df)-1, step=1)

    if st.button("Delete Row"):
        try:
            delete_row_from_table(table_choice, delete_index)
            st.success("Row deleted successfully. Refresh the page to see the update.")
        except Exception as e:
            st.error(f"Error: {e}")
