import smtplib
import imaplib
import ssl
def login(me, read_mail):
    password = "verysecure1337"
    context = ssl.create_default_context()
    port = 465
    if read_mail == True:#read mail
        with imaplib.IMAP4_SSL("imap.gmail.com",993) as server:
            server.login(me,password)
    else:#send mail
        with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
            server.login(me,password)
    return server
