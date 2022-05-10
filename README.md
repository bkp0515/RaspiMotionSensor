# RaspiMotionSensor
## A Raspberry Pi motion sensor using WiFi and MQTT
I used a raspberry pi zero w first generation and a HC-SR501 to create a motion sensor to turn my lights on and off.
The script was written in python and makes use of MQTT to communicate.

## What you need
This project makes use of a home assistant server to controll the IOT devices. I used the mqtt plugin on Home Assistant to be my broker and to setup the device in HASS. I used a Pi Zero W first generation which seem to be in short supply at the moment. The sensor module I used is the HC-SR501. I used three female to male jumper wires to connect the sensor to the pi so I did not have to use a breadboard. Circuit diagram is below

![CircuitDiagram](https://user-images.githubusercontent.com/91356620/167543975-d98bb77d-9ab6-4796-85d4-f1db7aaaaf51.png)

## How to Setup
__Please note that this project is not 100 percent accurate. The raspberry pi does not always push to the HASS server.__
I installed the latest version of raspbian lite to my raspberry pi zero w and setup ssh for programming. You could also use a keyboard and a monitor directly on the Pi if that is prefered. 
This program makes use of the Paho-MQTT library to install on the pi type 'pip3 install paho-mqtt' 
copy the test script to the pi, wire the sensor module and run the test script to make sure your sensor is working. Copy the motionSense script the pi, adjust the broker address to your HASS server and set the topic to something you will remeber. I used some formatting recomenneded in the guides I was using to learn about MQTT with python. Then you can edit your hass configuration file to setup a sensor to listen to the MQTT topic. Some more resources will be linked below that I used to setup the project.

## Resources
[MQTT in python](https://www.emqx.com/en/blog/how-to-use-mqtt-in-python)
[MQTT on HASS](https://www.home-assistant.io/integrations/mqtt/)
[Motion sensor I used](https://www.amazon.com/gp/product/B07KBWVJMP/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)
