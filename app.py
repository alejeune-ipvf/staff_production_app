import streamlit as st
import pandas as pd
from io import BytesIO

st.title('Staff production management')

tab1,tab2 = st.tabs(["Load, View and Edit Procedures","Load Init File and Create Logbook"])

with tab1:
    uploaded_file = st.file_uploader("Select the procedures catalog Excel file from your local machine.", type="xlsx")
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        edited_df = st.data_editor(df,num_rows="dynamic",hide_index=True)
        if st.button('Save to cache / Save changes to cache'):
            st.session_state["df"] = edited_df
            st.write("Changes saved in cache (and available in other tabs). Download the updated file to save them permanently.")
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                edited_df.to_excel(writer,index=False)
            st.download_button("Download updated file", data=buffer, file_name="updated_procedures.xlsx", mime="application/vnd.ms-excel")
with tab2:
    if "df" in st.session_state:
        st.write("WIP")
        st.write("Current procedure catalog in cache :")
        st.dataframe(st.session_state["df"])
    else:
        st.write("No procedures in cache, please upload a valid procedures catalog first.")