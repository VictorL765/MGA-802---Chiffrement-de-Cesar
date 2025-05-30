#Ce code sert à battir l'interface pour l'utilisateur

#Fonction afficher pour pouvoir modifier le style d'affichage si besoin
def afficher(message):
    print(message)

#Definition d'un interface laissant le choix a l'utilisateur de crypter ou decrypter son texte
def interface():
    afficher("Bienvenue dans le chiffrement de César")
    afficher("Souhaitez-vous crypter ou decrypter ?")

    choix=input("Tapez 'c' pour crypter ou 'd' pour decrypter : ").lower() #on garde a réponse en minuscule

#en cas d'une entrée différente de c ou d
    if choix not in ['c', 'd']:
        afficher("Choix invalide sortie du programme")
        return

#choix entre console et fichier
    afficher("Voulez vous utiliser votre fichier texte ou entrer votre texte dans la console")
    texte = input(" Entrez le texte: ")

    clef_connue=input(" Avez vous une clé ? (oui/non) : ").lower()

#si la clef est connue on appel crypter ou decrypter
    if clef_connue == "oui":
        cle= int(input("Entrez la clé :"))

        if choix == "c":
            from Cryptage_decryptage import crypter
            afficher(crypter(texte, cle))

        else:
            from Cryptage_decryptage import decrypte
            afficher(decrypter(texte, cle))

#sinon on fait appel a brute force
    else:
        from Bruteforce import bruteforce
        afficher("Decryptage par ... la force brute ! :")
        bruteforce(texte)



