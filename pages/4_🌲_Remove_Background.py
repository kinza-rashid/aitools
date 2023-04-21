from rembg import remove
from io import BytesIO
import streamlit as st
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title=" GRADIENT TECHNOLOGIES",
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
    st.title("🔮 :violet[G]RADIENT :violet[T]ECHNOLOGIES")
with c2:
    st.text("")
    st.text("")
    cbtn = st.button("Contact us")

st.divider()

st.header(' :green[🌲 Remove Background ]')
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
    col1, col2 = st.columns(2)

    # @st.cache_data

    def convert_image(img):
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        return byte_im

        # @st.cache_data

    def fix_image(upload):
        image = Image.open(upload)
        col1.subheader(":green[Original Image]")
        col1.image(image)

        edited = remove(image)

        col2.text("")
        col2.text("")

        col2.download_button(
            "  Download Edited Image", convert_image(
                edited), "fixed.png", "image/png", use_container_width=True
        )
        col2.text("")
        col2.text("")
        col2.text("")
        col2.subheader(":green[Edited Image]")

        col2.image(edited)

        # Create the file uploader
    my_upload = col1.file_uploader(
        "", type=["png", "jpg", "jpeg"])

    # Remove background
    if my_upload is not None:
        fix_image(upload=my_upload)
    else:
        fix_image("images/wpic.jpeg")
