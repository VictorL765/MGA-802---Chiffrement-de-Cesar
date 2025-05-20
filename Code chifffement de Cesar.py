import string

alphabet = string.ascii_lowercase



# fonction qui renvoie l'index de chaque lettre du mot
liste_index = []
def index_mot(liste) :
    for i in range (len(liste)) :
         index = alphabet.find(liste[i])
         liste_index.append(index)
         print(liste_index)

