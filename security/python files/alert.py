import serial
import smtplib
import ssl
from datetime import date
from email.mime.text import MIMEText
from from_arduino import stream

def write_file(file_path):
    fail = False
    try:        
        f = open(file_path,'a',encoding='utf-8')
        print("opened fine")
        data = stream()
        print("stream fine")
        f.write("Code: "+data[0]+"\nTemp: "+data[1]+" celsius\nHumidity: "+data[2]+"\n")
    except:
        fail = True
        print("failed writing")
    finally:
        f.close()
    return fail


def send_email(server,me,to):
    #ascii chars
    today = str(date.today())
    textfile = '/home/pi/Documents/'+today+'.txt'
    fail = write_file(textfile)
    if fail == False:
        fp = open(textfile, 'r')
    #create message
        msg = MIMEText(fp.read())
        fp.close()
        if msg.as_string()[0] == 1:
            
            msg['Subject'] = 'ALARM'
            msg['From'] = me
            msg['To'] = to
            server.sendmail(me,to,"ALARM TRIGGERED")
            server.close()
    
    
def alert():
    me = "bullyhack2020@gmail.com"
    to = "stephenjones0117@gmail.com"
    read_mail = False;
    port = 465
    password = 'verysecure1337'
    me = 'bullyhack2020@gmail.com'
    to = 'stephenjones0117@gmail.com'
    context = ssl.create_default_context()
    
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(me, password)
    send_email(server,me,to)
    