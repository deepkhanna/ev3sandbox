#!/usr/bin/env python3
from ev3dev2.sound import Sound
def mySpeech():
    sound=Sound()
    #text to speech
    sound.speak('I will destroy you! Beware Stranger!')
    sleep(1)

mySpeech()