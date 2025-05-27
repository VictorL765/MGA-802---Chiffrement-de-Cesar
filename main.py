import string


alphabet = string.ascii_lowercase
liste_index = []


#Fonction qui permet de lire un mot
def lecture_du_mot():
    #demande a l'utilisateur de rentrer le mot
    mot = input('Entrez le mot : ')
    # retourne la liste/chaine de caractère de mots
    return mot



# fonction qui renvoie l'index de chaque lettre du mot
def index_mot(mot) :
    liste_index = []
    for lettre in mot :
        index = alphabet.index(lettre)
        liste_index.append(index)
    return liste_index


mot = lecture_du_mot()
print(mot)
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
print(f'Le mot crypte est :{mot_crypte}')

#Déchiffre le mot crypter connaissant sa clef
def dechiffrage (mot_a_decrypte, cle):
    mot_decrypte ="" #Chaine de caractère vide qui servira à renvoyer le mot decrypté
    index_des_lettres2 = index_mot(mot_a_decrypte) # recupère les indices du mot à dechiffrer
    for k in range (len(index_des_lettres2)) : # boucle qui itère sur la longueur du mot à décrypter
        index_d=(index_des_lettres2[k] - cle) % 26 # Calage et rotation dans l'alphabet
        mot_decrypte += alphabet[index_d]
    return mot_decrypte

mot_decrypte = dechiffrage(mot, 3)
print(f'Le mot decrypte est : {mot_decrypte}')

