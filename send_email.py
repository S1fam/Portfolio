import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "s1fam0n3@gmail.com"
password = "azbychwijzpsbcyh"

reciever = "s1fam0n3@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Email from Portfolio app
How are you?
Hey, hi, hello.
Bye!
"""

with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, reciever, message)
