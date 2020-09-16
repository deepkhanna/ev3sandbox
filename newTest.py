#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sound import Sound
from sys import stderr
from time import sleep
ts = TouchSensor()
sound = Sound()
while True:
 if (ts.is_pressed):
    sound.speak('Ouch!')
    sleep(0.5)
    break