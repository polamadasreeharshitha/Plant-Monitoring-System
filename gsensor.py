#!/usr/bin/python
#import the libraries required
import sys
import Adafruit_DHT
import requests
import serial
import time
import RPi.GPIO as GPIO
import time
url="http://192.168.43.61:8084/get"
#Serial Communication transfers data from arduino to pi
ser = serial.Serial('/dev/ttyACM0',9600)
def Sensor_value():
     while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)  #temperature sensor value
        read_serial=ser.readline()
        s=str(read_serial)
        s=s.split(",")                          #retrieving the values
        rain_info_1 =s[0]           #raindrop sensor value
	soil_moisture=s[1]          #soilmoisture value
	soil1=s[2]
	motor=s[3]
	motor1=s[4]
	GPIO.setmode(GPIO.BCM)      #setting GPIO pin to broadcom mode
        TRIG = 23                   #GPIO pins 23 and 24 are connected TRIG and ECHO respectively
        ECHO = 24
        GPIO.setup(TRIG,GPIO.OUT)   #setting TRIG as output pin
        GPIO.setup(ECHO,GPIO.IN)    #setting ECHO as input pin
        GPIO.output(TRIG, False)    #Initialise TRIG to false
        time.sleep(2)
        #Generate an impulse 
        GPIO.output(TRIG, True)     #Initialise TRIG to true
        time.sleep(0.00001) 
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO)==0:      #pulse starting time
              pulse_start = time.time()
        while GPIO.input(ECHO)==1:      #pulse ending time
              pulse_end = time.time() 
        pulse_duration = pulse_end - pulse_start   #pulse duration
        distance = pulse_duration * 17150          #distance is calculated
        distance = round(distance, 2)              #calculated distance is rounded to 2 decimals
        water_lev=distance                         #obtained distance is stored in waterlevel
#values in sensor data are assigned into dictionary readings
	for i in range(1,3):
		data = {'i':i,'temperature':temperature,'humidity':humidity,'rain_info_1':rain_info_1,'soil_moisture':soil_moisture,'soil_moisture1':soil1,'water_lev':water_lev,'motor':motor,'motor1':motor}
        #sensor data is send to server using post method
		requests.get(url,params=data)
		print water_lev
		print temperature,humidity
		print rain_info_1,soil_moisture
		print soil1,motor1
        GPIO.cleanup()                       #reset ultrasonic sensor
Sensor_value()


