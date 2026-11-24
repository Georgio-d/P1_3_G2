# Imports go at the top
from microbit import *
import radio
cA = 0
cB = 0
lock =  False
dose = 0
ml = 50

# Code in a 'while True:' loop repeats forever
while True:
    # A+B held together -> unlock
    if button_a.is_pressed() and button_b.is_pressed():
        lock = True
        cA = 0
        cB = 0
        display.show(Image.YES)
        sleep(500)
        button_a.was_pressed()  # clear presses made by the combo
        button_b.was_pressed()

    elif lock:
        if button_a.was_pressed():
            cB = 0
            cA += 1
            if cA == 2:
                dose += ml
                cA = 0
                display.show(dose)

        if button_b.was_pressed():
            cA = 0
            cB += 1
            if cB == 2:
                dose -= ml
                cB = 0
                display.show(dose)
    if pin_logo.is_touched() and dose > 0:
        radio.send(str(dose))
        lock = False
        
