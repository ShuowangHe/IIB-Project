import serial
arduino = serial.Serial('/dev/cu.usbmodem14201',38400)
while True:
    data = arduino.readline()[:-2]
    if data:
        print(data)
