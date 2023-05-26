import streamlit as st

st.title("Contact me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email adress")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        massage = message + user_email
        print(button)
        print(" Buttoned ")
