#ce code sert dans le cas d'oublie de la clefs par l'utilisateur

import string
from Cryptage_decryptage import decrypter
from FichierRessourse import lire_fichier

#charger des mots courants depuis un fichier txt
def charger_mots_courants(fichier=#mots_courants.txt):
    try:
       contenu = lire_fichier(fichier)
       mots_courants = contenu.split[]
       return mots_courants
    except Exception as e:
       print(f"Erreur de chargarment des mots courants: {str(e)}")
       return []

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

