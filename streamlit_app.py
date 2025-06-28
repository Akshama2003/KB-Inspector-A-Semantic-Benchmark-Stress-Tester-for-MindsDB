import streamlit as st
from mindsdb_utils import create_kb, insert_data, semantic_query
import pandas as pd

st.title("🧠 MindsDB KB Inspector")

uploaded_file = st.file_uploader("Upload a JSON dataset", type=["json"])
if uploaded_file:
    df = pd.read_json(uploaded_file, lines=True)
    st.write("Preview:", df.head())

    if st.button("Create & Insert into KB"):
        create_kb("news_kb")
        insert_data("news_kb", df)
        st.success("Inserted into MindsDB!")

query = st.text_input("Semantic Query")
if st.button("Run Query"):
    results = semantic_query("news_kb", query)
    st.write("Results:", results)
