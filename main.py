import string
import os

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
    mot_decrypte += alphabet[index_d] #ajout des lettres
    return mot_decrypte

mot_decrypte = dechiffrage(mot, 3)
print(f'Le mot decrypte est : {mot_decrypte}')

#Fonction qui propose à l'utilisateur de choisir son fichier avec des mots
def choisir_fichier (fichier = "mots_pendu.txt", dossier = "/Users/elsakupfer/Documents/ETS/ETE/MGA802") :

    # teste si le fichier existe
    full_filename = os.path.join(dossier,fichier)
    if not os.path.isfile(full_filename):
        raise RuntimeError(f'Je ne trouve pas le fichier {full_filename} !')

     # Ouvre le fichier contenant les mots en mode lecture
    with open(full_filename, 'r', encoding='utf8') as f:
        # Lire le contenu du fichier
        words = f.read()

lecture_fichier = fichier()

#Fonction qui permet de choisir l'option de cryptage ou decryptage, interface utilisateur
def main() :


 # Décrypte le mot méthode force-brute
def dechiffrage(mot_a_decrypte):
    mot_decrypte = ""  # Chaine de caractère vide qui servira à renvoyer le mot decrypté
    index_des_lettres2 = index_mot(mot_a_decrypte)  # recupère les indices du mot à dechiffrer
    for k in range(len(index_des_lettres2)):  # boucle qui itère sur la longueur du mot à décrypter
        for cle in range (0,27) :
        index_d = (index_des_lettres2[k] - cle) % 26  # Calage et rotation dans l'alphabet
        mot_decrypte += alphabet[index_d]  # ajout des lettres
        print (f'Le mot decrypte est : {mot_decrypte}')
        question = input('Est ce que mot semble correcte ? (oui/non) :').lower()
        if question in ('oui') :
            print (f'Le mot decrypte valide est : {mot_decrypte}')
            break
        else :
            dechiffrage(mot_a_decrypte)
    return mot_decrypte

# Gérer les espaces, accents et caractère spécifique

#Améliore la performance du programme force-brute
#Utiliser les mots les plus courants de la la,gue française
# % (de, le, des, ...) verbes, ...
# if y a des indice qui permettent de faire ces types de mots --> les proposer en premier ?
# https://www.lingoda.com/blog/fr/les-mots-les-plus-utilises-en-francais/
# ou voir Word


def lire_texte_courant(fichier_c="mots_courants.txt", dossier_c="/Users/elsakupfer/PycharmProjects/MGA-802---Chiffrement-de-Cesar"):
    #full_filename = fichier_c
    full_filename = os.path.join(fichier_c, dossier_c)

    # teste si le fichier existe
    if not os.path.isfile(full_filename):
        raise RuntimeError(f'Je ne trouve pas le fichier {full_filename} !')

    # Ouvre le fichier contenant les mots en mode lecture
    with open(full_filename, 'r', encoding='utf8') as f:
        # Lire le contenu du fichier
        words = f.read()

        # retourne la liste de mots
        return words

fichier_c = input ('nom du fichier texte des mots courants.txt:')
dossier_c = input ('Chemin du dossier des mots courants:')
mot_courants=lire_texte_courant()