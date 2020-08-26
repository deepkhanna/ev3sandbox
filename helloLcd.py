#!/usr/bin/env python3
from time import sleep
from ev3dev2.display import Display
from textwrap import wrap

def show_text(string,font_name, font_width=15, font_height=24):
    lcd=Display()
    lcd.clear()
    strings=wrap(string, width=int(180/font_width))
    for i in range(len(strings)):
        x_val=89-font_width/2*(len(strings)/2-i)
        y_val=63-(font_height+1)*(len(strings)/2-i)
        lcd.text_pixels(strings[i], False, x_val, y_val, font=font_name)
    lcd.update()


my_text='The quick brown fox jumps over the lazy dog'

show_text(my_text, 'courB14', 9, 14)
sleep(5)

show_text(my_text, 'lutBS14', 9, 14)
sleep(5)

