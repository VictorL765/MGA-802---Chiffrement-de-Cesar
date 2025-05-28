#ce code sert à crypter/décrypter le teCryptagexte ou l'input d'entrée
import string
import unicodedata



alphabet = string.ascii_lowercase

#Pour retirer les accents on ce sert de l'outil necessaire page 8 du chiffrement de César
def enlever_caracteres_speciaux(texte):
    normalized_word=unicodedata.normalize('NFKD', texte)
    return ''.join(char for char in normalized_word if not unicodadata.combining(char))
