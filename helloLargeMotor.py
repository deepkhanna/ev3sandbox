#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B,OUTPUT_C
from ev3dev2.sound import Sound
from time import sleep
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM

def moveRight():
  rightLeg=LargeMotor(OUTPUT_B)
  rightLeg.on_for_seconds(speed=SpeedDPS(100), seconds=1)

def moveLeft():
  leftLeg=LargeMotor(OUTPUT_C)
  leftLeg.on_for_seconds(speed=SpeedDPS(100), seconds=1)

moveRight()
moveLeft()

## File name