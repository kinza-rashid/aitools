
import streamlit as st
import requests

st.set_page_config(
    page_title=" SOLVERA",
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
    st.title("🔮 :violet[SOLV]ERA")
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
    # st.form("contact us", clear_on_submit=True)
else:
    st.header(' :green[🔊 Text to Speech ]')
    st.divider()
    txt_input = st.text_input("Enter your text here 👇🏻")
    button = st.button("Generate Speech")
    st.divider()
    c1, c2 = st.columns((1, 1))
    with c1:
        st.text("")
        if button:
            if txt_input == "":
                st.text("Enter text prompt.")
            if button and (txt_input != ""):
                # if button:
                with st.spinner("Generating speech ..."):
                    response = requests.post("https://abidlabs-speak.hf.space/run/predict", json={
                        "data": [
                            txt_input,
                        ]}).json()
                    md = f"""
                        <audio controls>
                        <source src = "{response["data"][0]}" type = "audio/flac">
                        </audio>
                        """
                st.markdown(
                    md,
                    unsafe_allow_html=True,
                )
