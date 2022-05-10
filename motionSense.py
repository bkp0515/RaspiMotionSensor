#!/usr/bin/python3

import time #Import time library
import RPi.GPIO as GPIO #Import raspi gpio library
import paho.mqtt.client as mqtt #Import mqtt client library
import paho.mqtt.publish as publish #Import publish command

GPIO.setmode(GPIO.BOARD) #Set mode for GPIO
pir = 40 #Set the pin for the motion sensor
GPIO.setup(pir, GPIO.IN) #Make the pin an input

broker = "192.168.0.126" #define mqtt broker
state_topic = "home-assistant/basement/motion" #define mqtt topic
client = mqtt.Client("motionSensor", True) #Create new MQTT client
client.connect(broker) #Connect the client to the MQTT broker
client.publish(state_topic, "Idle") #Publish idle to server on startup
client.disconnect() #Disconnect from server while not in use

print ("Waiting for motion sensor to settle") #Print update to command line
time.sleep(2) #Give the motion sensor time to settle down
print ("Detecting motion") #Print update to command line

while True: #Create infinite loop
        if GPIO.input(pir): #Check if the sensor detects motion

                print ("Motion Detected!") #Print to command line motion is detected
                client.reconnect() #Reconnect to the server
                client.publish(state_topic, "Motion Detected!") #Publish to the server again
                client.disconnect() #Clean disconnect from the server
                time.sleep(180) #Wait to check again for motion before turning the lights back off
                if GPIO.input(pir) != 1: #Check for motion again
                        client.reconnect() #Reconnect to the server
                        client.publish(state_topic, "Idle") #Publish idle to the server to turn of lights
                        client.disconnect() #Clean disconnect from server
                        print ("Published Idle to server") #Notify the terminal that idle has been published
        time.sleep(0.1) #Allow the server some time before checking for motion again
