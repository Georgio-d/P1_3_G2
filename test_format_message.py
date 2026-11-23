types = {0x01: "connexion", 0x02: "lait", 0x03: "etat_eveil"}
etat_bebe = ["agite", "tres_agite", "endormi"]
#ce sont les états du bébé

def construire_message(type_msg, contenu):
    """
    Construit un message au format TLV : type|longueur|contenu.
    
    pre :  type_msg est un entier (int) qui identifie le type du message.
           contenu est une chaîne de caractères (str), éventuellement vide,
           qui ne contient pas le caractère "|".
    post : renvoie une chaîne (str) de la forme "type|longueur|contenu",
           où longueur est le nombre de caractères de contenu.         
    """
    longueur = len(contenu)
    return str(type_msg) + "|" + str(longueur) + "|" + contenu

assert construire_message(0x01, "connexion") == "1|9|connexion", "Test classique"
assert construire_message(0x02, "12") == "2|2|12", "Test classique"  
assert construire_message(0x01, "") == "1|0|", "Contenu vide"

print(construire_message(0x01, "connexion"))

def unformat_message(message):
    """
    pre :  message est une chaîne (str).
    post : si message est au format "type|longueur|contenu" et que longueur
           correspond bien au nombre de caractères de contenu, renvoie
           type_msg, contenu.
           Sinon, renvoie None.
    """
    message_liste = message.split("|")
    # message_liste contient type, longueur, contenu dans une liste 

    type_msg = int(message_liste[0])
    longueur_annoncee = int(message_liste[1])
    contenu = message_liste[2]

    if longueur_annoncee != len(contenu):
        return None
    #ça permet de vérifier si le message n'est pas corrompu et aussi pour les chiffremnets qu'on
    #devra faire 

    return type_msg, contenu

assert unformat_message("1|9|connexion") == (1, "connexion")
assert unformat_message("2|0|") == (2, ""), "Contenu vide"
assert unformat_message("2|9| ") == None, "Longueur incorrecte"
print (unformat_message("2|1|3"))

def interpreter_message(type_msg, contenu):
    """
    pre :  type_msg est un int, contenu est une str
           (voir unformat_message).
    post : effectue l'action correspondant au type du message
           (pour l'instant : affiche ce qui a été compris).
    """
    if type_msg not in types:
        print("Type inconnu")
        return
    
    if type_msg == 0x01:
        print("Connexion, challenge reçu : " + contenu)
    elif type_msg == 0x02:
        print("Lait : " + contenu + " doses") #le contenu est la quantité de biberons
        #Exemple : le parent a fait 3 biberons. Il envoie "2|1|3"
        #L'enfant le décode (type_msg = 2, contenu = "3") et cette branche affiche Lait : 3 doses.
    elif type_msg == 0x03:
        etat = etat_bebe[int(contenu)]
        #car le numéro arrive sous forme de string "1"
        # int() transforme le texte "1" en nombre 1,
        # puis on ouvre le tiroir, éléments correspondant dans la liste
        print("Etat du bebe : " + etat)