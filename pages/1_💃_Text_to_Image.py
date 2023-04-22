
import requests
import streamlit as st
import os
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
    st.header(' :green[💃 Text to Image  ]')
    st.divider()
    prompt = st.text_input("Enter text prompt here 👇🏻 ")

    button = st.button("Generate Image")

    st.divider()
    if button:
        if prompt == "":
            st.text("Enter suitable text prompt.")

        if button and prompt != "":
            with st.spinner(text="In progress..."):
                IMG_API = st.secrets["IMAGE_API"]
                API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
                headers = {
                    "Authorization": IMG_API}

                def text2image(payload):
                    response = requests.post(
                        API_URL, headers=headers, json=payload)
                    return response.content

                image = text2image(prompt)

                st.image(image, caption='Output Image')
                # st.balloons()
