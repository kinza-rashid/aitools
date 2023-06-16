
from urllib import response
import requests
import streamlit as st

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
    st.header(' :green[👨‍🦲 Dalai Lama  ]')
    st.divider()
    prompt = st.text_input("Example Prompt : Help the needy. Reply: Help the needy with money, advice, hope and compassion. ")

    button = st.button("Write")

    st.divider()
    if button:
        if prompt == "":
            st.text("Enter suitable text prompt.")

        if button and prompt != "":
            
            with st.spinner(text="Dalai lama is thinking ..."):
                DALAILAMA_API = st.secrets["DALAI_API"]

                API_URL = "https://api-inference.huggingface.co/models/huggingtweets/dalailama"
                headers = {
                    "Authorization": DALAILAMA_API}

                def query(payload):
                    response = requests.post(
                        API_URL, headers=headers, json=payload)
                    return response.json()

                output = query({
                    "inputs": prompt,
                })
            st.write("", output[0]["generated_text"])
