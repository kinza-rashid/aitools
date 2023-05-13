import streamlit as st
import webbrowser
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
    st.header("🌍 :green[Explore AI Tools & Services]")
    st.divider()
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14 = st.tabs(
        ["GPT-4", "Lablab", "Rytr", "Runway", "Lalal", "Boost AI", "Avatar", "Stable Diffusion", "Midjourney", "Synthesia", "My Character AI", "Adept AI", "Elai", "Luma Labs"])

    with c1:
        c1.subheader("GPT-4")
        col1, col2 = st.columns((2, 1))

        col1.markdown(
            'GPT-4 is the most advanced large language model from Open AI. GPT-4 can solve difficult problems with greater accuracy, thanks to its broader general knowledge and problem solving abilities')

        if col1.button("Explore GPT-4"):
            url = 'https://openai.com/product/gpt-4'
            col1.markdown(url, unsafe_allow_html=True)
            

        col2.image("images/gpt.jpeg")

    with c2:

        c2.subheader("Lablab")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'Community of Makers, building with state-of-the-art, modern Artificial Intelligence. lablab, is all about building a community of makers and innovators creating the AI Native future')

        if col1.button("Explore Lablab AI"):
            url = 'https://lablab.ai/'
            col1.markdown(url, unsafe_allow_html=True)
            
        col2.image("images/lablab.jpeg")

    with c3:
        c3.subheader(" Ryter")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'Rytr is an AI writing assistant that helps you create high-quality content, in just a few seconds, at a fraction of the cost!')

        if col1.button("Explore Rytr   "):
            url = 'https://rytr.me/'
            col1.markdown(url, unsafe_allow_html=True)
           
        col2.image("images/languages.jpg")
    with c4:
        c4.subheader(" Runway")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'Runway is a creative suite where AI is a collaborator and anything you can imagine can be created. Browse our full suite of 30+ AI Magic Tools that make it easier than ever to ideate, iterate and generate content')

        if col1.button("Explore Runway"):
            url = 'https://app.runwayml.com/'
            col1.markdown(url, unsafe_allow_html=True)
            
        col2.image("images/runway.jpg")
    with c5:
        c5.subheader("LALAL")
        col1, col2 = st.columns((2, 1))
        col1.markdown('A next-generation vocal remover and music source separation service for fast, easy and precise stem extraction. Remove vocal, instrumental, drums, bass, piano, electric guitar, acoustic guitar, and synthesizer tracks without quality loss')

        if col1.button("Explore LALAL"):
            url = 'https://lalal.ai'
            col1.markdown(url, unsafe_allow_html=True)
           
        col2.image("images/lalal.jpg")
    with c6:
        c6.subheader("BOOST AI")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'With Boost AI, you can improve customer satisfaction, cut costs and increase revenue of your company.Boost AI has connected cutting-edge generative AI to company data via our conversational AI platform to create the next generation of chat and voice bots and much more.')

        if col1.button("Explore BOOST AI"):
            url = 'https://www.boost.ai/'
            col1.markdown(url, unsafe_allow_html=True)
            
        col2.image("images/boost.jpg")

    with c7:
        c7.subheader("AVATAR")
        col1, col2 = st.columns((2, 1))
        col1.markdown('Transform yourself (or your dog, cat, or you and your bf/gf as a couple) into desert punk warriors, a zombie at Halloween, an Instagram model in the jungle, the main character in a video game to a fashion model. It is up to you to decide who you want to become! Your AI avatars will look just like you but in the styles you selec.')

        if col1.button("Explore Avatar"):
            url = 'https://avatarai.me/'
            col1.markdown(url, unsafe_allow_html=True)
            
        col2.image("images/avatar.jpg")
    with c8:
        c8.subheader("Stable Diffusion")
        col1, col2 = st.columns((2, 1))
        col1.markdown('Stable Diffusion is a latent text-to-image diffusion model capable of generating photo-realistic images given any text input, cultivates autonomous freedom to produce incredible imagery, empowers billions of people to create stunning art within seconds.')

        if col1.button("Explore Stable Diffusion"):
            url = 'https://stablediffusionweb.com/'
            col1.markdown(url, unsafe_allow_html=True)
            
        col2.image("images/stablediffusion.jpg")

    with c9:
        c9.subheader("Midjourney")
        col1, col2 = st.columns((2, 1))
        col1.markdown('Midjourney is an independent research lab exploring new mediums of thought and expanding the imaginative powers of the human species.We are a small self-funded team focused on design, human infrastructure, and AI. Join the Midjourney community on Discord or the Web, where thousands collaborate to create new worlds, fantastic characters, and unique imagery from short text descriptions.')

        if col1.button("Explore Midjourney"):
            url = 'https://www.midjourney.com'
            col1.markdown(url, unsafe_allow_html=True)
           
        col2.image("images/midjourney.jpg")
    with c10:
        c10.subheader("Synthesia")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'AI video creation platform where professional videos can be created in 15 minutes ! Say goodbye to cameras, microphones and actors.')

        if col1.button("Explore Synthesia"):
            url = 'https://www.synthesia.io/'
            col1.markdown(url, unsafe_allow_html=True)
            
        col2.image("images/synthesia.jpg")
    with c11:
        c11.subheader("My Character AI")
        col1, col2 = st.columns((2, 1))
        col1.markdown('A dApp built on the AI protocol that leverages the CharacterGPT Multimodal AI system to generate realistic, intelligent, and interactive AI characters.')

        if col1.button("Explore My Character AI"):
            url = 'https://mycharacter.ai/'
            col1.markdown(url, unsafe_allow_html=True)
           
        col2.image("images/mycharacter.jpg")
    with c12:
        c12.subheader("Adept AI")
        col1, col2 = st.columns((2, 1))
        col1.markdown('AI has moved at an incredible pace in the last few years. Scaling up Transformers has led to remarkable capabilities in language(e.g., GPT-3, PaLM, Chinchilla), code(e.g., Codex, AlphaCode), and image generation(e.g., DALL-E, Imagen).At Adept, we are building the next frontier of models that can take actions in the digital world—that’s why we’re excited to introduce our first large model, Action Transformer(ACT-1).')

        if col1.button("Explore Adept AI"):
            url = 'https://www.adept.ai/act'
            col1.markdown(url, unsafe_allow_html=True)
            
        col2.markdown("ACT-1 is a large-scale Transformer trained to use digital tools. It is recently taught how to use a web browser. Right now, it is hooked up to a Chrome extension which allows ACT-1 to observe what is happening in the browser and take certain actions, like clicking, typing, and scrolling, etc. The observation is a custom “rendering” of the browser viewport that is meant to generalize across websites, and the action space is the UI elements available on the page.")
    with c13:
        c13.subheader("Elai")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'Avatars and video generation tool using AI technologies.')

        if col1.button("Explore ELai"):
            url = 'https://app.elai.io'
            col1.markdown(url, unsafe_allow_html=True)
            
        col2.image("images/elai.jpg")
    with c14:
        c14.subheader("Luma Labs")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'Capture in lifelike 3D. Unmatched photorealism, reflections, and details. The future of VFX is now, for everyone! Photoreal Game Assets Capture unparalleled quality assets with a phone. Export to any game engine')

        if col1.button("Explore Luma Labs"):
            url = 'https://lumalabs.ai/'
            col1.markdown(url, unsafe_allow_html=True)
            
        col2.image("images/lumalabs.jpg")

    cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10, cc11, cc12, cc13 = st.tabs([
        "Genei", "Deep Swap", "Word Tune", "Text Blaze", "Iris", "Descript", "Otter", "Fireflies", "Quilbot", "My Heritage", "AI Writer", "Pictory", "Stability"])
    with cc1:
        cc1.subheader("Genei")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'Research faster with genei Automatically summarise background reading and produce blogs, articles, and reports faster')

        if col1.button("Genei"):
            url = 'https://www.genei.io/'
            col1.markdown(url, unsafe_allow_html=True)
           
        col2.image("images/genei.jpeg")

    with cc2:
        cc2.subheader("Deep Swap")
        col1, col2 = st.columns((2, 1))
        col1.markdown('Deepswap - AI Face Swap Online App Deepswap.ai is an online AI face swap app to generate faceswap videos, photos, and GIFs. Over 150 million users make funny face swapping here, including movie role refacing, gender swaps, face memes, etc. Spoof your friends now!')

        if col1.button("Explore Deep Swap"):
            url = 'https://www.deepswap.ai/'
            col1.markdown(url, unsafe_allow_html=True)
           
        col2.image("images/swap.jpg")
    with cc3:
        cc3.subheader("Word Tune")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'Your thoughts in words Say exactly what you mean through clear, compelling and authentic writing')

        if col1.button("Explore Word Tune"):
            url = 'https://www.wordtune.com/'
            col1.markdown(url, unsafe_allow_html=True)
           
        col2.image("images/wordtune.jpg")
    with cc4:
        cc4.subheader("Text Blaze")
        col1, col2 = st.columns((2, 1))
        col1.markdown('Eliminate repetitive typing and mistakes. Easy-to-use templates with endless customizability and powerful automation. All with full control at your fingertips')

        if col1.button("Explore Text Blaze"):
            url = 'https://blaze.today/'
            col1.markdown(url, unsafe_allow_html=True)
           
        col2.image("images/blaze.jpg")

    with cc5:
        cc5.subheader("Iris")
        col1, col2 = st.columns((2, 1))
        col1.markdown('A comprehensive platform for all your research processing: Smart search and a wide range of smart filters, reading list analysis, auto-generated summaries, autonomous extraction and systematizing of data. An award-winning AI engine for scientific text understanding. Our algorithms for text similarity, tabular data extraction, domain-specific entity representation learning and entity disambiguation and linking measure up to the best in the world. On top of that our machine builds a comprehensive knowledge graph containing all entities and their linkages to allow humans to learn from it, use it and also give feedback to the system. Applying these on scientific and technical text is a complicated challenge few others can achieve')

        if col1.button("Explore Iris"):
            url = 'https://iris.ai/'
            col1.markdown(url, unsafe_allow_html=True)
            
        col2.image("images/iris.jpg")
    with cc6:
        cc6.subheader("Descript")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'One tool for full workflow. Descript is the only tool you need to write, record, transcribe, edit, collaborate, and share your videos and podcasts')

        if col1.button("Explore Descript"):
            url = 'https://www.descript.com/'
            col1.markdown(url, unsafe_allow_html=True)
            
        col2.image("images/descript.jpg")
    with cc7:
        cc7.subheader("Otter")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'An AI meeting assistant that records audio, writes notes, automatically captures slides, and generates summaries.')

        if col1.button("Explore Otter"):
            url = 'https://otter.ai/'
            col1.markdown(url, unsafe_allow_html=True)
            
        col2.image("images/otter.jpg")
    with cc8:
        cc8.subheader("Fireflies")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'Automate your meeting notes. Fireflies.ai helps your team record, transcribe, search, and analyze voice conversations.')

        if col1.button("Fireflies"):
            url = 'https://fireflies.ai/'
            col1.markdown(url, unsafe_allow_html=True)
            
        col2.image("images/fireflies.jpg")
    with cc9:
        cc9.subheader("Quilbot")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'Whether you are writing emails, essays, or social media posts, QuillBot has your back')

        if col1.button("Explore Quilbot"):
            url = 'https://quillbot.com/'
            col1.markdown(url, unsafe_allow_html=True)
           

        col2.image("images/quilbot.jpg")

    with cc10:
        cc10.subheader("My Heritage")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'Animate your family photos Animate the faces in your family photos with amazing technology. Experience your family history like never before!')

        if col1.button("Explore My Heritage"):
            url = 'https://www.myheritage.com/deep-nostalgia'
            col1.markdown(url, unsafe_allow_html=True)
           
        col2.image("images/myheritage.jpg")

    with cc11:
        cc11.subheader("AI Writer")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'Generate Accurate, Relevant & Trustable Content in Minutes.')

        if col1.button("Explore AI Writer"):
            url = 'https://ai-writer.com/'
            col1.markdown(url, unsafe_allow_html=True)
           
        col2.image("images/writer.jpg")
    with cc12:
        cc12.subheader("Pictory")
        col1, col2 = st.columns((2, 1))
        col1.markdown(
            'Automatically create short, highly-sharable branded videos from your long form content.')

        if col1.button("Explore Pictory"):
            url = 'http://pictory.ai'
            col1.markdown(url, unsafe_allow_html=True)
           
        col2.image("images/pictory.jpg")

    with cc13:
        cc13.subheader("Stability")
        col1, col2 = st.columns((2, 1))
        col1.markdown('Open Source Models. We put control in your hands with open source models. Dream studio - Tap into the power of our generative text-to-image suite to create new and unique designs.')

        if col1.button("Explore Stability"):
            url = 'https://stability.ai/'
            col1.markdown(url, unsafe_allow_html=True)
           
        col2.image("images/stability.jpg")
