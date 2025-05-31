#Lancer le Chiffrement de Cesar

from Interface import *

interface()

renouveler = input('Voulez-vous recommencer ? (oui/non):').lower()
if renouveler == "oui":
    interface()
else:
    quit()