#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.sound import Sound
from time import sleep

def weaponRobo():
    sound=Sound()
    sound.speak('Kill Kill!')
    mm=MediumMotor(OUTPUT_A)
    mm.on_for_rotations(50, 1) # Do 1 rotation with 50% speed
    sleep(0.1)
    mm.on_for_rotations(-50, 1) # Do 1 rotation with reverse 50% speed


weaponRobo()

