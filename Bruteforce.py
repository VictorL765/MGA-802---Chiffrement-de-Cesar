#ce code sert dans le cas d'oublie de la clefs par l'utilisateur

import string
from Cryptage_decryptage import decrypter
import os

#mots_courants = [
   # "le", "la", "et", "un", "une", "est", "dans", "en", "il", "elle", "ce", "pour", "qui",
   # "sur", "pas", "plus", "avec", "tout", "mais", "nous", "vous", "comme", "bien", "fait"
#]

alphabet = string.ascii_lowercase
def lire_texte(fichier="mots_courants.txt",texte="mots_pendu.txt"):

    question = input('Voulez-vous utiliser votre propre fichier ? (oui/non) :')
    if question=='oui' :
        fichier = str(input("Entrez le nom du fichier, n'oubliez pas .txt :"))

    else :
        print('ok')
    lecture_fichier = fichier
    lecture_texte=texte

    # teste si le fichier existe
    if not os.path.isfile(lecture_fichier):
        raise RuntimeError(f'Je ne trouve pas le fichier {lecture_fichier} !')

    # Ouvre le fichier contenant les mots en mode lecture
    with open(lecture_fichier, 'r', encoding='utf8') as f:
        # Lire le contenu du fichier
        word1 = f.read()
        words = word1.split()


    with open(lecture_texte, 'r', encoding='utf8') as f:
        # Lire le contenu du fichier
        texte_a_dechiffrer1=f.read()
        texte_a_dechiffrer = texte_a_dechiffrer1.split()

        # retourne la liste de mots
        return words, texte_a_dechiffrer

mots_courants, texte_a_decrypter=lire_texte()







'''''
def lire_texte():

    lecture_fichier = input(r"Entrez le chemin du fichier texte :")

    # teste si le fichier existe
    if not os.path.isfile(lecture_fichier):
        raise RuntimeError(f'Je ne trouve pas le fichier {lecture_fichier} !')

    # Ouvre le fichier contenant les mots en mode lecture
    with open(lecture_fichier, 'r', encoding='utf8') as f:
        # Lire le contenu du fichier
        words = f.read()

        # retourne la liste de mots
        return words

lire_texte()

'''''


def brute_force(texte):
    for cle in range(1, 26):
        texte_a_tester = decrypter(texte, cle)
        for mot in mots_courants:
            if mot in texte_a_tester:
                print(f"Mot courant trouvé : '{mot}', avec la clé : {cle}")
                print(f"Message déchiffré :\n{texte_a_tester}")

                reponse_utilisateur = input("est ce que le message est correct ? 'o' pour oui, 'n' pour non : ")

                if reponse_utilisateur == "o":
                    print("Message confirmé")
                    return

                else:
                    print("On continue avec une autre clé")

    print("Aucun mot courant détecté.")

texte_a_decrypter = ' '.join(texte_a_decrypter)
brute_force(texte_a_decrypter)
