import streamlit as st
from PIL import Image

st.set_page_config(
    page_title=" SOLVER.AI",
    page_icon="☸️",
    layout="wide",
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
c1, c2 = st.columns((7, 1))
with c1:
    st.title("🔮 SOLVER :violet[AI]")
with c2:
    st.text("")
    st.text("")
    cbtn = st.button("Contact us")

st.divider()
a = 2

if cbtn and (a != 4):
    a = 4
    st.header("Contact us ! ")
    contact_form = """
        <form action = "https://formsubmit.co/rabhatti75@gmail.com" method = "POST">
        <input type="hidden" name="_captcha" value="false">
        <input type = "text" name = "name" placeholder="Your name" required>
        <input type="email" name = "email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send email</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style/style.css")

else:
    st.subheader("Try free AI solutions !")
    c1, c2, c3 = st.columns((1, 1, 1))
    c1.subheader(":violet[Text to Image]")

    text2image = Image.open("images/text2image.jpeg")
    c1.image(
        text2image, caption='Generated with prompt: Flowers along the river side with mountains in the background')

    c2.subheader(":violet[Poetry]")
    c2.markdown(
        ":green[Restless like a bird in the cage]  of night,I pace the floor and cannot rest; I have lived my life in a lonely way,And now I can only wait.The wind is blowing from across the sea, And it brings strange tales to me;Of men with sorrows like mine—and worse—Who cannot sleep or cease.")
    c3.subheader(":violet[Text to Speech]")
    c3.image("images/text2speech.jpg")

    st.subheader(":violet[Essay Writing]")
    st.image("images/essay.jpg")
    st.subheader(":violet[Remove Background]")
    st.image("images/removebackground.jpg")
    st.subheader(":violet[Future Works]")
    st.markdown("This website is a work in progress and it shall be updated continously in future. Other free AI technologies shall be integrated and shared with users.")
