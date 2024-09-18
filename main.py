import streamlit as st

# Define the pages
PAGES = {
    "Home": "home",
    "Play 2048": "game",
    "Play Powerline": "game2",
    "Play Snake.io": "snake",
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
        import home
        home.run()
    elif st.session_state.page == "game":
        import game
        game.run()
    elif st.session_state.page == "game2":
        import game2
        game2.run()
    elif st.session_state.page == "snake":
        import snake
        snake.run()

if __name__ == "__main__":
    main()
