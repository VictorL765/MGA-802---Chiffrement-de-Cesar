#Ce code sert à battir l'interface pour l'utilisateur

from FichierRessource import lire_fichier
from Cryptage_decryptage import crypter
from Cryptage_decryptage import decrypter
from Bruteforce import brute_force
from time import perf_counter


#Fonction afficher pour pouvoir modifier le style d'affichage si besoin
def afficher(message):
    print(message)

#Definition d'un interface laissant le choix a l'utilisateur de crypter ou decrypter son texte
def interface():
    texte = None #initialise la variable pour éviter des warings plus tard

    afficher("Bienvenue dans le chiffrement de César")
    afficher("Souhaitez-vous crypter ou decrypter ?")

    choix=input("Tapez 'c' pour crypter ou 'd' pour decrypter : ").lower() #on garde la réponse en minuscule

#en cas d'une entrée différente de c ou d
    if choix not in ['c', 'd']:
        afficher("Choix invalide sortie du programme")
        return

#choix entre console et fichier
    afficher("Voulez vous utiliser votre fichier texte ou entrer votre texte dans la console")
    source=input("Tapez 'c' ou 'f': ").lower()

    if source == "c":
       texte = input(" Entrez le texte: ")

    elif source == "f":
        nom_fichier = input("Tapez 'nom_fichier': ").lower()
        # Si le fichier n'existe pas ou qu'une erreur se produit, on affiche l'erreur et on arrete l'execution.
        try:
            texte = lire_fichier(nom_fichier)
        except Exception as e:    #https://stackoverflow.com/questions/18982610/difference-between-except-and-except-exception-as-e
            afficher(str(e))
            return

    clef_connue=input(" Avez vous une clé ? (oui/non) : ").lower()

#si la clef est connue on appel crypter ou decrypter
    if clef_connue == "oui":
        cle= int(input("Entrez la clé :"))

        if choix == "c":
            afficher(crypter(texte, cle))

        else:
            afficher(decrypter(texte, cle))

#sinon on fait appel a brute force
    else:
        afficher("Decryptage par ... la force brute !:")

        tic = perf_counter()  # Demarrage du chrono
        brute_force(texte)
        toc = perf_counter()  # Fin du chrono

        print(f"temps d'execution de la fonction brute force : {toc - tic}  [s]")




