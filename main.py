import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

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
    "Apps": "app",
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
    elif st.session_state.page == "app":
        play_app()

def home():
    st.title("Welcome to CR7 Games! (Suuuuui!!!)")
    st.write("Click the button below to open proxy!")
    st.link_button("Proxy", "https://gndrt5-8080.csb.app")
    st.link_button("Live Chat", "https://m59wy3-5000.csb.app/")

def play_2048():
    st.title('Play 2048')

    # URL of the game or webpage you want to embed
    game_url = 'https://gndrt5-8080.csb.app/service/https://2048game.com/'

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
    game_url = 'https://gndrt5-8080.csb.app/service/https://slope2.online/'

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
    game_url = 'https://gndrt5-8080.csb.app/service/https://backroomsgame.io/'

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
    game_url = 'https://gndrt5-8080.csb.app/service/https://basketball-stars.io/'

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
    game_url = 'https://gndrt5-8080.csb.app/service/https://geometrygame.org/'

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
    game_url = 'https://gndrt5-8080.csb.app/service/https://leveldevil.io/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_app():
    st.title('Apps')

    st.link_button("Crazy Games", "https://rtqpnd-8000.csb.app/portal?auth=kl828rs")
    st.link_button("Now.gg", "https://rtqpnd-8000.csb.app/portal?auth=q32jakr")
    st.link_button("Chess.com", "https://rtqpnd-8000.csb.app/portal?auth=f4fw9wb")
    st.link_button("Tiktok", "https://rtqpnd-8000.csb.app/portal?auth=7w4jjkm")
    st.link_button("CoolMath Games", "https://rtqpnd-8000.csb.app/portal?auth=bicqrgu")
    st.link_button("9amine", "https://rtqpnd-8000.csb.app/portal?auth=jfa05at")
    st.link_button("SFlix Movies", "https://rtqpnd-8000.csb.app/portal?auth=513v99m")
    st.link_button('Netflix', "https://rtqpnd-8000.csb.app/portal?auth=85jitel")
    st.link_button("Extra Games", "https://5nv5pz-8000.csb.appxm/gms")
    st.link_button("Better Proxy", "https://5nv5pz-8000.csb.app")
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_trial():
    st.title('Play Oregon Trial')

    # URL of the game or webpage you want to embed
    game_url = 'https://gndrt5-8080.csb.app/service/https://oregontrail.ws/games/the-oregon-trail/'

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
