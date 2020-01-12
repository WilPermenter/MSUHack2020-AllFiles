import serial
from email_command import read_mail
#double check the tty
#1 on 2 off

def get_input():
    return read_mail()

def command1(ser):
    ser.write(str.encode('0'))
    
def command2(ser):
    ser.write(str.encode('1'))
    
def command3(ser):
    ser.write(str.encode('2'))

def send_command(seri):
    ser = serial.Serial(seri,9600)
    user_input = get_input()
    print(user_input)
    if input == "0.":
        command1(ser)
    elif input == "1.":
        command2(ser)
    elif input == "2.":
        command3(ser)
send_command("/dev/ttyACM0")