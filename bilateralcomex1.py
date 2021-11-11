import serial
import time
import numpy as np
serialcomm = serial.Serial('/dev/ttyACM0', 9600)

serialcomm.timeout = 1
data=[]

while True:

    i = str(1.2)

    if i == "Done":

        print('finished')

        break

    serialcomm.write(i.encode())

    time.sleep(0.1)
    s=serialcomm.readline().decode('ascii')
    for i in range(0,len(s)-1,2):
        print(chr(int(s[i])*10 + int(s[i + 1])))


serialcomm.close()
