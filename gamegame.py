import streamlit as st
import streamlit.components.v1 as components

# Define the pages
PAGES = {
    "Home": "home",
    "Play 2048": "game",
    "Play Powerline": "game2",
    "Play Snake.io": "snake",
    "Play Wings.io": "Wing",
    "Play Slither.io": "Slither"
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

def home():
    st.title("Welcome to the Game Portal")
    st.write("Click the button below to play 2048!")

    # Button to navigate to the game page
    if st.button('Play 2048'):
        st.session_state.page = 'game'

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

def play_powerline():
    st.title('Play Powerline')

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



if __name__ == "__main__":
    main()
