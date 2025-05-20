import string


alphabet = string.ascii_lowercase
liste_index = []

def lecture_du_mot():
    mot = input('Entrez le mot : ')
    print(mot)
    # Transforme la chaine de caracteres en liste
    # le saut de ligne sert de separateur de champs
    #liste_de_caractere = mot.split('\n')

    # retourne la liste de mots
    return mot


# fonction qui renvoie l'index de chaque lettre du mot
def index_mot(mot) :
    liste_index = []
    for char in mot :
        index = alphabet.index(char)
        liste_index.append(index)
        #index = alphabet.index(liste[i])
    print(liste_index)

mot = lecture_du_mot()
index_mot(mot)



