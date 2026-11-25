# Imports go at the top
from microbit import *
import radio

radio.on()
radio.config(channel=7, address=0x12345678, group=200)

doses = 0

# image au debut pour voir que c'est le microbit enfant
display.show(Image.HAPPY)
sleep(1000)
display.clear()

while True:
    # on regarde si le parent a envoye un message
    msg = radio.receive()
    if msg:
        liste = msg.split("|")
        # on verifie que le message est bien en 3 parties et pas coupe
        if len(liste) == 3 and int(liste[1]) == len(liste[2]):
            # si le type est 2 c'est le lait
            if int(liste[0]) == 2:
                doses = int(liste[2])

    # quand on appuie sur A ca affiche le nombre de doses
    if button_a.was_pressed():
        display.scroll("Lait:" + str(doses))