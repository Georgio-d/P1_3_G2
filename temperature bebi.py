# Imports go at the top
from microbit import *
import radio
radio.on()


# Code in a 'while True:' loop repeats forever
while True:
    t = temperature()
    print(t)
    if t <= 16 :
        radio.send('4')
        print("cold")
    elif t > 16 and t< 24:
        radio.send('5')
        print('warm')
    else :
        radio.send('3')
        print('hot')