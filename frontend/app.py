import streamlit as st

st.set_page_config(
    page_title="Enterprise Deep Research Agent"
)

st.title("Enterprise Deep Research Agent")

query = st.text_input(
    "Ask anything..."
)

if query:
    st.write(query)