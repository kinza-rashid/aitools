
import streamlit as st
from streamlit_option_menu import option_menu
from sentence_transformers import SentenceTransformer  # ok with py 3.9.13
import pinecone  # pip3 install datasets

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
    st.header(' :green[🖋️ Essay Writing ]')
    st.divider()
    prompt = st.text_input("Enter text prompt here 👇🏻", "")
    button = st.button("Write Essay ")
    st.divider()
    st.text("")
    if button:
        if prompt == "":
            st.text("Enter text prompt.")
        if button and (prompt != ""):
            with st.spinner(text="Generating essay ..."):
                # if button:
                retriever = SentenceTransformer(
                    'sentence-transformers/multi-qa-MiniLM-L6-cos-v1')

                pinecone.init(
                    api_key='97079bd8-7f8d-481f-acc5-1d616aea75fc', environment='us-central1-gcp')

                index = pinecone.Index('squad')

                if prompt != "":
                    xq = retriever.encode([prompt]).tolist()
                    xc = index.query(xq, top_k=5,
                                     include_metadata=True)
                    for context in xc['matches']:
                        st.write(f"{context['metadata']}")
