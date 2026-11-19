def format_message():
    return str(Type) + "|" + str(a) + "|" + contenu
               
def unformat_message(message):
    message = format_message()
    message_liste = message.split("|")
    for a in message_liste:
        if a[0] == "1":
            Type = 0x01
            contenu = "Etablissement de connexion"
        elif a[0] == "2":
            Type = 0x02
            contenu = "Quantité de lait"
        elif a[0] == "3":
            Type = 0x03
            contenu = "Etat d’éveil du nourrisson"       
    return "Type de message : " + str(Type) + "| " + contenu

        
def reception_message(Type):   
    if Type == 0x01:
        contenu = "Etablissement de connexion"
    elif Type == 0x02:
        contenu = "Quantité de lait"
    elif Type == 0x03:
        contenu = "Etat d’éveil du nourrisson"

Type = 0x02
contenu = "Quantité de lait"
a = len(contenu)
message = format_message()
print(message)
message2 = message.split("|")

print(unformat_message(message2))
    

