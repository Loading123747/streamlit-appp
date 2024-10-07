import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

cr = Image.open('cmn.jpeg')
cr7 = Image.open("Ronaldo.jpeg")
# Define the pages
PAGES = {
    "Home": "home",
    "Play 2048": "game",
    "Play Backrooms": "game2",
    "Play Snake.io": "snake",
    "Play Basketball Stars": "Wing",
    "Play Slope": "Slither",
    "Play Geometry Dash": "geo",
    "Play Level Devil": "level",
    "Play Oregon Trial Game": "trial",
    "Your Games": "dev"
}

def main():
    st.link_button("🚨🚨EMERGENCY!(Click if the teacher is near)🚨🚨", "https://www.aleks.com/login")
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
    elif st.session_state.page == "trial":
        play_trial()

def home():
    st.title("Welcome to CR7 Games! (Suuuuui!!!)")
    st.write("Click the button below to open proxy!")
    st.link_button("Proxy", "https://dddjtd-8080.csb.app/")
    st.link_button("Live Chat", "https://dp67gr-8080.csb.app/")

def play_2048():
    st.title('Play 2048')

    # URL of the game or webpage you want to embed
    game_url = 'https://r82sm7-8080.csb.app/service/hvtrs8%2F-224%3Agcmg.aoo%2F/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_Slither():
    st.title('Play Slope')

    # URL of the game or webpage you want to embed
    game_url = 'https://ilovecrayons.hectorhector.com/portal?auth=nhkt1he'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)
    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_powerline():
    st.title('Play BackRooms')

    # URL of the game or webpage you want to embed
    game_url = 'https://fdmnrn-8080.csb.app/service/hvtrs8%2F-snoremnnile%2Collkng%2F%60aakpommq/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'


def play_Wing():
    st.title('Play Basketball Stars')

    # URL of the game or webpage you want to embed
    game_url = 'https://fdmnrn-8080.csb.app/service/hvtrs8%2F-bcsievbcln-qtcrq.ko-/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
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
    game_url = 'https://r82sm7-8080.csb.app/service/hvtrs8%2F-ggooevr%7Bgcmg.mre%2F/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
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

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_trial():
    st.title('Play Oregon Trial')

    # URL of the game or webpage you want to embed
    game_url = 'https://fdmnrn-8080.csb.app/service/hvtrs8%2F-opeeoltpakl%2Cwq%2F/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

left_column, right_column = st.columns(2)
if __name__ == "__main__":
    main()
