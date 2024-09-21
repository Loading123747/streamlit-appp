import streamlit as st

def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["Person"])[0]


st.set_page_config(page_title="Welcome")

PERSON_NAME = get_person_name()
st.header(f"Welcome, {PERSON_NAME}!", anchor=False)
st.subheader("Use this link to acces the website and use that browser and everything will be unblocked")
st.subheader("https://fdmnrn-8080.csb.app/")
