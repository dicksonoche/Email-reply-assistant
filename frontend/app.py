import streamlit as st
import requests

st.title("Professional Email Reply Drafter")

query = st.text_area("Enter customer query (e.g., 'My iPhone screen is cracked'):")

if st.button("Generate Reply"):
    if query:
        try:
            response = requests.post("http://localhost:8000/draft_reply", json={"text": query})
            response.raise_for_status()
            reply = response.json()["reply"]
            st.write("Drafted Reply:")
            st.write(reply)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a query.")