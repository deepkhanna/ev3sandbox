#!/usr/bin/env python3
from ev3dev2.led import Leds
from time import sleep

def myLed(side="LEFT"):
    """ 
    Function to set LED. Function has an input for side. 
    """
    leds=Leds()
    leds.set_color(side, 'ORANGE')
    sleep(10)

myLed()  # When you do not pass any value/side, it would take it as LEFT, because we define function like that
myLed("RIGHT")  # When you pass a value, it would  NOT take the default value of "LEFT" that is in function definiation.