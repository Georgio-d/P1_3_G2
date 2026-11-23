# Imports go at the top
from microbit import *
import music

#compteur de doses des parent
doses = 0
while True:

    #imaginons ils veulent tout recommencer ou qqch comme ça 
    if button_a.is_pressed() and button_b.is_pressed():
        doses = 0
        button_a.was_pressed()   #c'est pour "supprimer" la note "A a été appuyé"
        button_b.was_pressed()   #idem
        display.scroll("0")
        music.play(music.BA_DING)

    #ajoute une dose
    elif button_a.was_pressed():
        doses+= 1
        display.scroll(str(doses))
        music.play(music.POWER_UP)
    

    #supprime une dose (missclik)
    elif button_b.was_pressed():
        if doses > 0 :
         doses -=1
         display.scroll(str(doses))
         music.play(music.POWER_DOWN)
        elif doses == 0:
            display.scroll(str(doses))
              
        
    #voir le total de doses
    elif pin_logo.is_touched():
        display.scroll(str(doses))
        music.pitch(185, 1000)
        
    sleep(100)
    
#is_pressed() pose la question : est-ce que le bouton est appuyé à l'instant T ? Si c'est le cas, ça répond True, sinon False.

#was_pressed() pose la question : est-ce que le bouton a été appuyé depuis le dernier appel qu'on a fait à cette fonction ? S'il a bien été appuyé à un moment, ça renvoie True. Une fois que c'est fait, il oublie : il n'enregistre plus la valeur, et ça revient à dire que le bouton n'a plus été touché. Donc si, dans notre code, on appelle la fonction une nouvelle fois, elle renvoie False, parce que le bouton n'a pas été réappuyé entre-temps.
#j'ai utilisé ça quand on appuie sur a et b pour pas que le microbit ne le retienne