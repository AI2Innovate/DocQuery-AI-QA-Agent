import streamlit as st
import requests

st.title("LLM-Powered FAQ Assistant")
question = st.text_input("Ask a question about the docs")

if st.button("Ask") and question:
    response = requests.post("http://localhost:8000/ask", json={"question": question})
    st.write("Answer:", response.json()['answer'])
