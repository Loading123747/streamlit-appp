import streamlit as st
import streamlit.components.v1 as components

def run():
    st.title('Play 2048')

    # URL of the game or webpage you want to embed
    game_url = 'https://play2048.co/'

    # HTML code to embed the game in an iframe
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;"></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'
