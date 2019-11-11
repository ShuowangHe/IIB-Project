import serial
import time
import csv

arduino = serial.Serial('/dev/cu.usbmodem14201',38400)
start_time = time.time()
array = []
i=0
while True:
    data = arduino.readline()[:-2]
    if data:
        elapsed_time = time.time()-start_time
        mass = float(data[-9:-3])
        array.append([elapsed_time,mass])
        print(elapsed_time,mass)
        with open('Output.csv','a',) as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow([elapsed_time,mass])
