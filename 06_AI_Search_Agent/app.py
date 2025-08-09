import streamlit as st
from search_agent import query_documents

st.title("AI-powered Enterprise Search Agent")
st.caption("Ask questions across internal files, policies, or wikis")

query = st.text_input("Enter your question.....")

if query:
    result = query_documents(query)
    st.subheader("AI-Generated Answer")
    st.text_area("Search Response", result, height=500)