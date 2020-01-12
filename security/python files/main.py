from alert import alert
from talking import send_command

def main():
    seri = "/dev/ttyACM0"
    while True:
        try: #check mail
            send_command(seri)
        except:
            print("No commands given")
        
        try:#check arduino and alert user if needed
            alert(seri)
        except:
            print("No new emails")

#if __name__ == "__main__":
main() 