import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# Define the pages
PAGES = {
    "Home": "home",
    "Play 2048": "game",
    "Play Powerline": "game2",
    "Play Snake.io": "snake",
    "Play Wings.io": "Wing",
    "Play Slither.io": "Slither",
    "Play Geometry Dash": "geo",
    "Play Level Devil": "level",
    "Your Games": "dev"
}

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    # Set session state for page navigation
    st.session_state.page = PAGES[selection]

    # Load the selected page
    if st.session_state.page == "home":
        home()
    elif st.session_state.page == "game":
        play_2048()
    elif st.session_state.page == "game2":
        play_powerline()
    elif st.session_state.page == "Wing":
        play_Wing()
    elif st.session_state.page == "Slither":
        play_Slither()
    elif st.session_state.page == "geo":
        play_geo()
    elif st.session_state.page == "dev":
        play_dev()
    elif st.session_state.page == "level":
        play_level()

def home():
    st.link_button("🚨🚨EMERGENCY!(Click if the teacher is near)🚨🚨", "https://www.aleks.com/login")
    st.title("Welcome to CR7 Games! (Suuuuui!!!)")
    st.write("Click the link below to open proxy!")
    st.write("https://fdmnrn-8080.csb.app")

def play_2048():
    st.title('Play 2048')

    # URL of the game or webpage you want to embed
    game_url = 'https://fdmnrn-8080.csb.app/service/hvtrs8%2F-pna%7B224%3A.ao-/'

    # HTML code to embed the game in an iframe
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;"></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_Slither():
    st.title('Play Slither.io')

    # URL of the game or webpage you want to embed
    game_url = 'https://fdmnrn-8080.csb.app/service/hvtrs8%2F-snivhgreaoe%2Cim%2F/'

    # HTML code to embed the game in an iframe
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;"></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_powerline():
    st.title('Play Powerline.io')

    # URL of the game or webpage you want to embed
    game_url = 'https://fdmnrn-8080.csb.app/service/hvtr%3A-%2Froueplkng.ko/'

    # HTML code to embed the game in an iframe
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;"></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'


def play_Wing():
    st.title('Play Wings.io')

    # URL of the game or webpage you want to embed
    game_url = 'https://fdmnrn-8080.csb.app/service/hvtr%3A-%2Fuilgq.ko/'

    # HTML code to embed the game in an iframe
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;"></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_dev():
    st.title("Your Games")
    st.subheader("Submit requests for your favorite games")
    st.header("Get in touch with me")
    contact_form = """
    <form action="https://formsubmit.co/Panvi83@outlook.com" method="POST">
        <input type="text" name="name" placeholder = "Your Name" required>
        <input type="email" name="email" placeholder = "Your Email" required>
        <textarea name="message" placeholder="Your favorite game" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_geo():
    st.title('Play Geometry Dash')

    # URL of the game or webpage you want to embed
    game_url = 'https://fdmnrn-8080.csb.app/service/hvtrs8%2F-ggooevr%7Bgcmg.mre%2F/'

    # HTML code to embed the game in an iframe
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;"></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'


def play_level():
    st.title('Play Level Devil')

    # URL of the game or webpage you want to embed
    game_url = 'https://gamepluto.com/game/infinite-craft/'

    # HTML code to embed the game in an iframe
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;"></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

if __name__ == "__main__":
    main()
