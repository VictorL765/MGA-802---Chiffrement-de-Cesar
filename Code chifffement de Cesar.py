
def lecture_du_mot():
    mot = input('Entrez le mot : ')
    print(mot)
        # Transforme la chaine de caracteres en liste
        # le saut de ligne sert de separateur de champs
    liste_de_caractere = mot.split('\n')

    # retourne la liste de mots
    return liste_de_caractere

# fonction qui renvoie l'index de chaque lettre du mot
liste_index = []
def index_mot(liste) :
    for i in range (len(liste)) :
         index = alphabet.find(liste[i])
         liste_index.append(index)
         print(liste_index)

