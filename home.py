import streamlit as st

def run():
    st.title("Welcome to the Game Portal")
    st.write("Click the button below to play 2048!")

    # Button to navigate to the game page
    if st.button('Play 2048'):
        st.session_state.page = 'game'
