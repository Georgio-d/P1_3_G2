# Imports go at the top
from microbit import *

if endormi:
    display.show(Image.ASLEEP)
    sleep(400)
    display.scroll('endormi')    

if agiter:
    display.show(Image('00900:'
                       '00900:'
                       '00900:'
                       '00000:'
                       '00900'))
    display.scroll('agiter')    

if très agiter:
    display.show(Image('90909:'
                       '90909:'
                       '90909:'
                       '00009:'
                       '90909'))
    display.scroll('très agiter') 