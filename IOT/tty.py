import serial
import time
s=serial.Serial("/dev/serial0",9600)
while 1:
    print("Testing")
    s.write(str.encode('Testing......'))
    receive_data=s.read()
    time.sleep(0.03)
    if s.inWaiting():
        data_left=s.inWaiting()
        receive_data=s.read(data_left)
        print("Testing 2")
        print(receive_data)
        s.write(receive_data)
