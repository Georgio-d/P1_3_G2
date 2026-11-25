from microbit import *
import radio
radio.config(channel=7, address=0x12345678, group=200)  
radio.on()

while True:
    # on mesure tt le temps mm sans message
    x_total = 0
    y_total = 0
    for i in range(100):
        y = accelerometer.get_y()
        y_total += y
        x = accelerometer.get_x()
        x_total += x
        sleep(10)
    y_moy = y_total / 100
    x_moy = x_total / 100
    print(x_moy)
    print(y_moy)
    # j'ai changer le format en TLV car type 3 = etat du bebe (comme ca tt va avec tt)
    if x_moy < 500 and x_moy > -500 and y_moy > -300 and y_moy < 300:
        print("endormi")
        radio.send("3|1|0")
    elif x_moy > -800 and x_moy < 800 and y_moy < 500 and y_moy > -500:
        print("agite")
        radio.send("3|1|1")
    else:
        print("tres agite")
        radio.send("3|1|2")
    sleep(2000) 