import serial



#C start E end
#code, temp humid, end
def stream():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    print("what the fuck")
    scan = True
    skip = True
    data = ["","",""]
    i = -1
    while scan is True:
        bit = str(ser.read())[2]
        #print(bit)
        if bit == 'C' or skip == False:
            skip = False
            if bit != 'C' and bit != 'T' and bit != 'H' and bit != 'E':
                print("bit: ",str(bit))
                data[i] += bit
            elif bit == 'E':
                scan = False
            else:
                i+=1
                print("index: ",i)
    return data