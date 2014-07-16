#Python example for SoftUart https://github.com/zoon81/avr-softuart
#This program based on pyserial libs.
#Receive 5 string from avr over UART that contain \n\r on the end of each string.
#After sending "0" 3 times,and reveiving back this as formated string 

import serial
import time

ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.xonxoff = False
ser.rtscts = False
ser.dsrdtr = False
ser.baudrate = 2400
ser.timeout = None

ser.open()
ser.setDTR(False)

ser.flushInput()
ser.flushOutput()

messange = ser.readline()
print messange 
messange = ser.readline()
print messange 
messange = ser.readline()
print messange 
messange = ser.readline()
print messange 
messange = ser.readline()
print messange 

time.sleep(1)
ser.write("000");
messange = ser.readline()
print messange 
messange = ser.readline()
print messange 
messange = ser.readline()
print messange 