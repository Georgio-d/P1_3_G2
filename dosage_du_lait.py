# Imports go at the top
from microbit import *
import radio
cA = 0
cB = 0
lock =  False
dose = 0
ml = 50
A = button_a.is_pressed()
B = button_b.is_pressed()
# Code in a 'while True:' loop repeats forever
while True:
    if A and B:
        display.show(Image.YES)
        lock =  True 
        cA = 0 
        cB = 0
        if A and lock:
            cB = 0 
            cA +=1
            if cA == 2:
                dose = dose + ml
                cA = 0 
                display.show(dose)
        if B and lock:
            cB += 1
            cA = 0
            if cB == 2:
                dose = dose - ml
                cB = 0
                display.show(dose)   
    if pin_logo.is_touched() and dose > 0:
        radio.send(str(dose))
        lock = False
        
