# Imports go at the top
from microbit import *
import radio
radio.config(group=2)#il y a pas que cette  configuration il ya en plus l'adresse=0x12345678 et la chanel qui etant è par defaut 7 qui representes la frequences entre les microbites qui se comporte comme des talkie walkie


# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        radio.on()
        radio.send('bebe')
