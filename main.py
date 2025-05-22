import string


alphabet = string.ascii_lowercase
liste_index = []

#Fonction qui permet de lire un mot
def lecture_du_mot():
    #demande a l'utilisateur de rentrer le mot
    mot = input('Entrez le mot : ')
    print(mot)
    # retourne la liste de mots
    return mot


# fonction qui renvoie l'index de chaque lettre du mot
def index_mot(mot) :
    liste_index = []
    for char in mot :
        index = alphabet.index(char)
        liste_index.append(index)
        #index = alphabet.index(liste[i])
    return liste_index


mot = lecture_du_mot()
index = index_mot(mot)
print(index)


def chiffrage(mot_a_crypter, cle):
    mot_crypte ="" #Chaine de caractere vide qui servira a renvoyer le mot crypte
    index_des_lettres = index_mot(mot_a_crypter) #Recuperer les indices des lettres du mot a chiffrer
    for i in range(len(index_des_lettres)): #Boucle qui itère sur la longueur de la liste
        index =(index_des_lettres[i] + cle ) % 26 #decalage + on fait une rotation dans l'alphabet
        mot_crypte += alphabet[index] #convertit l'index décalé en lettre dans la chaine de caractere vide
    return mot_crypte

mot_crypte = chiffrage(mot, 2)
print(mot_crypte)