import streamlit as st
import send_email

st.title("Contact me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email adress")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email} 
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        sending = send_email.send_email(message)
        if sending == "error":
            st.write("you have to enter your message without ř/á/í/ů.. symbols")
        else:
            st.info("your email has been sent")
