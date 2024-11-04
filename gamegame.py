import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

#r = Image.open("download.jpeg")
# Define the pages
PAGES = {
    "Home": "home",
    "Play 2048": "game",
    "Play 5 Nights At Freddy's": "game2",
    "Play Basketball Stars": "Wing",
    "Play Slope": "Slither",
    "Play Granny": "geo",
    "Play Bitlife": "level",
    "Play Level Devil": "trial",
    "Play Basket Random": "basket",
    "Play Crossy Road": "cross",
    "Play Retro Bowl": "retro",
    "Play Getaway Shootout": "get",
    "Play 1v1 LOL": "lol",
    "Play Uno": "uno",
    "Information": "info",
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
    elif st.session_state.page == "basket":
        play_basket()
    elif st.session_state.page == "cross":
        play_cross()
    elif st.session_state.page == "info":
        play_info()
    elif st.session_state.page == "retro":
        play_retro()
    elif st.session_state.page == "get":
        play_get()
    elif st.session_state.page == "lol":
        play_lol()
    elif st.session_state.page == "uno":
        play_uno()

def home():
    st.title("Welcome to CR7 Games! (Suuuuui!!!)")
   # st.image(r, width=300)
    st.write("Before you start using the website read the notes in the information tab for information on how to use the website")
    st.write("Click the button below to open proxy!")
    st.link_button("Proxy", "https://special-potato-4jgw6j4jgrg93jvw-8080.app.github.dev/")
    st.link_button("Live Chat", "https://q57pzh-8080.cb.app/")

def play_2048():
    st.title('Play 2048')

    # URL of the game or webpage you want to embed
    game_url = 'https://6glct3-8080.csb.app/web/_aHR0cHM6Ly8yMDQ4Z2FtZS5jb20=_/'

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
    game_url = 'https://6glct3-8080.csb.app/web/_aHR0cHM6Ly9zbG9wZTMuY29t_/'

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
    st.title('Play 5 Nights At Freddys')

    # URL of the game or webpage you want to embed
    game_url = 'https://6glct3-8080.csb.app/web/_aHR0cHM6Ly9maXZlbmlnaHRzYXRmcmVkZHlzMy5jb20=_/'

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
    game_url = 'https://6glct3-8080.csb.app/web/_aHR0cHM6Ly9iYXNrZXRiYWxsc3RhcnMtZ2FtZS5pbw==_/'

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
    st.title('Play Granny')

    # URL of the game or webpage you want to embed
    game_url = 'https://6glct3-8080.csb.app/web/_aHR0cHM6Ly9ncmFubnktZ2FtZXMuY29t_/'

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
    st.title('Play Bitlife')

    # URL of the game or webpage you want to embed
    game_url = 'https://6glct3-8080.csb.app/web/_aHR0cHM6Ly9iYXNrZXRiYWxsc3RhcnMtZ2FtZS5pbw==_/bitlife'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'


def play_basket():
    st.title('Play Basket Random')

    # URL of the game or webpage you want to embed
    game_url = 'https://6glct3-8080.csb.app/web/_aHR0cHM6Ly9iYXNrZXRiYWxsc3RhcnMtZ2FtZS5pbw==_/basket-random'

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
    st.write("If it doesn't work, in the url (in the proxy below the actual url. it is in dark bule) enter the url (proxy url) shown on top of the buttons")
    st.title("            ")
    st.write("https://www.crazygames.com/")
    st.link_button("Crazy Games", "https://ominous-space-potato-g4w5xjxv649cv4q9-8000.app.github.dev/live?auth=mjr4sin")
    st.write("https://now.gg/")
    st.link_button("Now.gg", "https://ominous-space-potato-g4w5xjxv649cv4q9-8000.app.github.dev/live?auth=ln31ksk")
    st.write("https://www.chess.com/")
    st.link_button("Chess.com", "https://ominous-space-potato-g4w5xjxv649cv4q9-8000.app.github.dev/live?auth=jd8uf23")
    st.write("https://www.tiktok.com/explore")
    st.link_button("Tiktok", "https://ominous-space-potato-g4w5xjxv649cv4q9-8000.app.github.dev/live?auth=s03pvfq")
    st.write("https://www.coolmathgames.com/")
    st.link_button("CoolMath Games", "https://ominous-space-potato-g4w5xjxv649cv4q9-8000.app.github.dev/live?auth=on8ui0v")
    st.write("https://9amime.com/")
    st.link_button("9amine", "https://ominous-space-potato-g4w5xjxv649cv4q9-8000.app.github.dev/live?auth=l031ddm")
    st.write("https://SFlix.com/")
    st.link_button("SFlix Movies", "https://ominous-space-potato-g4w5xjxv649cv4q9-8000.app.github.dev/live?auth=8qm5t6r")
    st.write("https://Netflix.com/")
    st.link_button('Netflix', "https://ominous-space-potato-g4w5xjxv649cv4q9-8000.app.github.dev/live?auth=cgp5cbs")
    st.link_button("Extra Games", "https://ominous-space-potato-g4w5xjxv649cv4q9-8000.app.github.dev/gms")
    st.link_button("Better Proxy", "https://ominous-space-potato-g4w5xjxv649cv4q9-8000.app.github.dev/")
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_trial():
    st.title('Play Level Devil')

    # URL of the game or webpage you want to embed
    game_url = 'https://6glct3-8080.csb.app/web/_aHR0cHM6Ly93d3cuc25va2lkby5jb20=_/game/level-devil'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_cross():
    st.title('Play Crossy Road')

    # URL of the game or webpage you want to embed
    game_url = 'https://6glct3-8080.csb.app/web/_aHR0cHM6Ly93d3cuc25va2lkby5jb20=_/game/crossy-road'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_retro():
    st.title('Play Retro Bowl')

    # URL of the game or webpage you want to embed
    game_url = 'https://6glct3-8080.csb.app/web/_aHR0cHM6Ly9yZXRyb2Jvd2wubWU=_/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_get():
    st.title('Play Getaway Shootout')

    # URL of the game or webpage you want to embed
    game_url = 'https://6glct3-8080.csb.app/web/_aHR0cHM6Ly9nZXRhd2F5LXNob290b3V0LmNvbQ==_/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'


def play_lol():
    st.title('Play 1v1 LOL')

    # URL of the game or webpage you want to embed
    st.write("somtimes it is a bit glitchy and if it is go to this link: https://6glct3-8080.csb.app/web/_aHR0cHM6Ly8xdjFsb2wubWU=_/")
    st.write("to play with friends or 1v1 other real people click on the plus icon and then click create party. share the code to play with friends (only works with 2 people including you, or don't share to play by your self or online player) then click play only party leader can click play")
    game_url = 'https://6glct3-8080.csb.app/web/_aHR0cHM6Ly8xdjFsb2wubWU=_/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_uno():
    st.title('Play Uno')

    # URL of the game or webpage you want to embed
    game_url = 'https://j6glct3-8080.csb.app/web/_aHR0cHM6Ly9nZXRhd2F5LXNob290b3V0LmNvbQ==_/uno-online'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'


def play_info():
    st.title("Information")
    st.subheader("Notes before we begin:")
    st.write("This website is still under development and is sometimes a bit glitchly. when you open or use any of the games give it some time to load and if it does not work reload the page a few times. New games will be added often so if you think that his website has very little games or games that you don't like, suggest some games to me in the your games tab. I also wish that you use the live chat website in the home page so that you can talk with other people that are using the website(or the people using the chat app) it is also realtime and I will be on it 24/7(I hope)")
    st.subheader("Information:")
    st.write("If you want to use the proxy in the home tab know that it does not work most of the time due to development, so if you want to use the proxy go to the apps tab and use the better proxy. If you do use the proxy in the home tab you need a url or it won't work(By the way I Fixed the proxy in the home tab so it will work fine) For more games there is also a link to my other website for more games. Just like I said in the notes if the games don't work reload the website a few times, the same goes for the proxy that the extra games. If you want to play any of the games in the fullscreen version scroll down in the game window and you will see a fullscreen button. I hope that you enjoy the website and good luck")
left_column, right_column = st.columns(2)
if __name__ == "__main__":
    main()
