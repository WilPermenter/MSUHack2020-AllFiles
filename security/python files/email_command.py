import imaplib
import smtplib
import time
import email
from login import login
def read_mail():
    me = "bullyhack2020@gmail.com"
    password = "verysecure1337"
    server = imaplib.IMAP4_SSL('imap.gmail.com',993)
    server.login(me,password)
    server.select('inbox')
    try:
        result,data = server.uid('search',None,'(UNSEEN)')
        inbox_item_list = data[0].split()
        most_recent = inbox_item_list[-1]
        result2,email_data = server.uid('fetch', most_recent, '(RFC822)')
        raw_email = email_data[0][1].decode("UTF-8")
        email_message = email.message_from_string(raw_email)
        
        if email_message.is_multipart():
            for payload in email_message.get_payload():
                for part in email_message.walk():
                    if (part.get_content_type() == 'text/plain') and (part.get('Content-Disposition') is None):
                        print("multipart")
                        return part.get_payload()
                break
        else:
            text = f"{email_message.get_payload(decode=True)}"
            html = text.replace("b'", "")
            h = html2text.HTML2Text()
            h.ignore_links = True
            output = (h.handle(f'''{html}''').replace("\\r\\n", ""))
            output = output.replace("'", "")
            print("singlepart")
            return output
    except:
        return ""
