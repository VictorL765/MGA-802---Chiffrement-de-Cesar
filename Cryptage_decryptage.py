#ce code sert à crypter/décrypter le teCryptagexte ou l'input d'entrée
import string
import unicodedata



alphabet = string.ascii_lowercase

#Pour retirer les accents on ce sert de l'outil necessaire page 8 du chiffrement de César
def enlever_caracteres_speciaux(texte):
    normalized_word=unicodedata.normalize('NFKD', texte)
    return ''.join(char for char in normalized_word if not unicodedata.combining(char))


#Fonction crypter le texte selon le chiffrement de César avec la clé donnée
def crypter(texte, cle):
    texte = enlever_caracteres_speciaux(texte.lower()) #mettre le texte en minuscule par defaut
    texte_crypte= ""

    for lettre in texte:
        if lettre in alphabet:
            index= (alphabet.index(lettre)+cle) % 26 #pour les 26 lettres
            texte_crypte += alphabet[index]
        else:
            texte_crypte += lettre

    return texte_crypte

crypter()

#Pour decrypter le texte chiffré avec la clé on réutilise la fonction crypter en inversant le décalage
def decrypter(texte, cle):
    return crypter(texte, -cle)

decrypter(texte, )