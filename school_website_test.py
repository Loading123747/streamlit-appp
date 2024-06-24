import streamlit as st

st.header("welcome")
st.subheader("go to this website for game: https://4wt6q5-8080.csb.app/")

def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["Werdio"])[0]


st.set_page_config(page_title="Welcome")

PERSON_NAME = get_person_name()
st.header(f"Welcome, {PERSON_NAME}!", anchor=False)
