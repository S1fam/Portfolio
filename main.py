import streamlit as st

st.set_page_config(layout="wide")  # adjusts website to occupy whole width

column1, column2 = st.columns(2)  # setting two columns

with column1:  # puts content into first (left) column
    st.image("images/MYphoto.jpg")

m = st.markdown("""
<style>
div.stTitle{
font-size: 60px;
}
</style>""", unsafe_allow_html=True)

with column2:
    st.title("Jaroslav Ištvan")
    content = """
    Hello, my name is Jaroslav. I am student of information technology on Faculty of Information Technology at
    Brno's University of Technology. I have created this webpage as part of my Python learning journey. This webpage
    is supposed to showcase Python projects i've built, in other words, to serve as my portfolio.
    I have been interested in Python for few years now, actively learning the language portion of that time.
    My help and inspiration being online courses aswell as scripting languages course at my university. Among these
    things, my high school graduation work was about Python, that being a series of tutorials where i explained
    the basics of the language. \n
    A little about me. Im 20 years old, from Czech Republic. I enjoy working out and playing videogames, 
    also travelling appeals to me, the picture of
    me you see is from a trip me and my friends took to Mallorca - Spain, where we attempted to conquer the GR 221
    mountain trail in summer, almost succesfully, however that story would be more fitting for a blog page :).
    """
    st.info(content)

contact_content = '<p style="font-family:Helvetica; font-size: 20px; font-weight: semi-bold">' \
                  'Bellow you can find some of the apps i have built in Python, Feel free to contact me.</p>'

st.markdown(contact_content, unsafe_allow_html=True)
