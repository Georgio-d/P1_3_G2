from microbit import *
import music

def alerter(etat):
    """
    pre :  etat est un entier: 0 (endormi), 1 (agite) ou 2 (tres agite).
    post : affiche etat du bebe sur l'ecran et fait un son
           de plus en plus fort en fonction de si cest urgent
    """
    if etat == 0:
        # le bb dort : que une image pas de son
        display.show(Image.ASLEEP)
        sleep(1000)
        display.scroll("endormi")

    elif etat == 1:
        # agite
        display.show(Image('00900:'
                           '00900:'
                           '00900:'
                           '00000:'
                           '00900'))
        music.play(music.BA_DING)
        display.scroll("agite")

    elif etat == 2:
        # tres agite : repeter 3x comme ca les parents viennent vite
        display.show(Image('90909:'
                           '90909:'
                           '90909:'
                           '00000:'
                           '90909'))
        for i in range(3):
            music.play(["A5:2", "E5:2"])
            music.play(["A5:2", "E5:2"])
            sleep(200)
        display.scroll("tres agite")

# Test  simulation etat avec les bouton
while True:
    if button_a.was_pressed():
        alerter(0)
    elif button_b.was_pressed():
        alerter(1)
    elif pin_logo.is_touched():
        alerter(2)
    sleep(100)