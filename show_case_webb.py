def load_lottieurl(url):
    r = requests.ge(url)
    if r.status_code !=200:
        return None
    return r.json()
st.set_page_config(page_title="About Me", page_icon=":partying_face:")

st.subheader("Hi my name is Praneeth :wave:")
st.write("my full name is Praneeth Chandra Mandula. I am 12 years old(turning 13) and go to Rose Hill Middle school. My hobbys is to code, play outside, play video games, and watch TV")
st.write("If you want to learn to code a website like this go here 👉 https://forms.gle/Wi9ad41sf7vH7L2k6    ")

st.write("----")
left_column, right_column = st.columns(2)
with left_column:
    st.header("what I do")
    st.write("##")
    st.write(
        """"
        I am a 12 year old kid who codes python. I also help run a youtube channel with my cousin.
        In my channel I post Traveling stuff that you should subscribe to. 
    """)
    st.write("Youtube Channel: (https://www.youtube.com/@Samosasoulmates)")

lottie = load_lottieurl = ("https://lottie.host/afc27642-a837-49c2-8004-51e0fca63531/bj4cQkKCUp.json")

with right_column:
    st.lottie(lottie, height = 300, key = "Youtube")


with st.container():

    st.write("---")
    st.header("Get in touch with me")
    contact_form = """
    <form action="https://formsubmit.co/Panvi83@outlook.com" method="POST">
        <input type="text" name="name" placeholder = "Your Name" required>
        <input type="email" name="email" placeholder = "Your Email" required>
        <textarea name="message" placeholder="Your message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
