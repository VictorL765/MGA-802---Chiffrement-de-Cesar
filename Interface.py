#Ce code sert à battir l'interface pour l'utilisateur



#Fonction afficher pour pouvoir modifier le style d'affichage si besoin
def afficher(message):
    print(message)

#Definition d'un interface laissant le choix a l'utilisateur de crypter ou decrypter son texte
def interface():
    afficher("Bienvenue dans le chiffrement de César")
    afficher("Souhaitez-vous crypter ou decrypter ?")

    choix=input("Tapez 'c' pour crypter ou 'd' pour decrypter : ").lower() #on garde la réponse en minuscule

#en cas d'une entrée différente de c ou d
    if choix not in ['c', 'd']:
        afficher("Choix invalide sortie du programme")
        return

    texte = input(" Entrez le texte: ")

    clef_connue=input(" Avez vous une clé ? (oui/non) : ").lower()

#si la clef est connue on appel crypter ou decrypter
    if clef_connue == "oui":
        cle= int(input("Entrez la clé :"))

        if choix == "c":
            from Cryptage_decryptage import crypter
            afficher(crypter(texte, cle))

        else:
            from Cryptage_decryptage import decrypter
            afficher(decrypter(texte, cle))

#sinon on fait appel a brute force
    else:
        afficher("Decryptage par ... la force brute ! :")
        from Bruteforce import brute_force
        brute_force(texte)



    renouveler=input('Voulez-vous recommencer ? (oui/non):').lower()
    if renouveler == "oui":
        interface()
    else :
        quit()

interface()