#ce code sert dans le cas d'oublie de la clefs par l'utilisateur

import string
from Cryptage_decryptage import decrypter
import os



alphabet = string.ascii_lowercase

# Lis le fichier texte comportant les mots courants français et le fichier à décrypter
def lire_texte(fichier="mots_courants.txt",texte="mots_pendu.txt"):

    question = input('Voulez-vous utiliser votre propre fichier ? (oui/non) :')

    if question=='oui' :
        #Demande le nom du fichier à décrypter en format texte
        fichier = str(input("Entrez le nom du fichier, n'oubliez pas .txt :"))

    else :
        print('ok')
    lecture_fichier = fichier # la variable lescture_fichier prend le fichier des mots courants français
    lecture_texte=texte # la variable lescture_texte prend le fichier par défaut à décrypter

    # teste si le fichier existe
    if not os.path.isfile(lecture_fichier):
        raise RuntimeError(f'Je ne trouve pas le fichier {lecture_fichier} !')

    # Ouvre le fichier contenant les mots en mode lecture
    with open(lecture_fichier, 'r', encoding='utf8') as f:
        # Lire le contenu du fichier
        word1 = f.read()
        words = word1.split() #sépare les chaines de caractère lorsqu'il y a un espace, permet d'identifier les mots


    with open(lecture_texte, 'r', encoding='utf8') as f:
        # Lire le contenu du fichier
        texte_a_dechiffrer1=f.read()
        texte_a_dechiffrer = texte_a_dechiffrer1.split()

        # retourne la liste de mots
        return words, texte_a_dechiffrer #retourne les fichiers comprenant les mots avec

mots_courants, texte_a_decrypter=lire_texte()





def brute_force(texte):
    for cle in range(0, 25): #test les clefs possibles sur les lettres de l'alphabet
        texte_a_tester = decrypter(texte, cle)
        for mot in mots_courants:
            if mot in texte_a_tester: #test si un des mots courant est présent
                print(f"Mot courant trouvé : '{mot}', avec la clé : {cle}") #précise le mot qui a permis au programme de trouver la clef et sa clef
                print(f"Message déchiffré :\n{texte_a_tester}") # renvoie l'intégralité du texte déchiffré


                reponse_utilisateur = input("est ce que le message est correct ? 'o' pour oui, 'n' pour non : ") #demande à l'utilisateur de valider ou non

                if reponse_utilisateur == "o":
                    print("Message confirmé")
                    return

                else:
                    print("On continue avec une autre clé")
                    break #permet de recommencer une boucle for pour tester une nouvelle clef

    print("Aucun mot courant détecté.")

texte_a_decrypter = ' '.join(texte_a_decrypter) #permet de transformé la variable liste, texte_a_decrypter en chaine de caractère
brute_force(texte_a_decrypter) #execute le programme
brute_force(texte_a_decrypter) #execute le programme
