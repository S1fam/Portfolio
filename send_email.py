import smtplib
import ssl
import os  # to store enviroment variable


def send_email(message):
    try:
        host = "smtp.gmail.com"
        port = 465
        username = "s1fam0n3@gmail.com"
        password = os.getenv("PASSWORD")
        reciever = "s1fam0n3@gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, reciever, message)
    except UnicodeError:
        return "error"
