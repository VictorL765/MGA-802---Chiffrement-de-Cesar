#ce code sert dans le cas d'oublie de la clefs par l'utilisateur

import string
from Cryptage_decryptage import decrypter

mots_courants = [
    "le", "la", "et", "un", "une", "est", "dans", "en", "il", "elle", "ce", "pour", "qui",
    "sur", "pas", "plus", "avec", "tout", "mais", "nous", "vous", "comme", "bien", "fait"
]

alphabet = string.ascii_lowercase

def lire_texte_courant():
    full_filename = input(r"Entrez le chemin du fichier texte :\n")

    # teste si le fichier existe
    if not os.path.isfile(full_filename):
        raise RuntimeError(f'Je ne trouve pas le fichier {full_filename} !')

    # Ouvre le fichier contenant les mots en mode lecture
    with open(full_filename, 'r', encoding='utf8') as f:
        # Lire le contenu du fichier
        words = f.read()

        # retourne la liste de mots
        return words



def lire_texte():
    import os
    full_filename = input(r"Entrez le chemin du fichier texte :\n")

    # teste si le fichier existe
    if not os.path.isfile(full_filename):
        raise RuntimeError(f'Je ne trouve pas le fichier {full_filename} !')

    # Ouvre le fichier contenant les mots en mode lecture
    with open(full_filename, 'r', encoding='utf8') as f:
        # Lire le contenu du fichier
        words = f.read()

        # retourne la liste de mots
        return words


def brute_force(texte):
    for cle in range(1, 26):
        texte_a_teste = decrypter(texte, cle)
        for mot in mots_courants:
            if mot in texte_a_teste:
                print(f"Mot courant trouvé : '{mot}', avec la clé : {cle}")
                print(f"Message déchiffré :\n{texte_a_teste}")

                reponse_utilisateur = input("est ce que le message est correct ? 'o' pour oui, 'n' pour non ")

                if reponse_utilisateur == "o":
                    print("Message confirmé")
                    return

                else:
                    print("On continue avec une autre clé")

    print("Aucun mot courant détecté.")
