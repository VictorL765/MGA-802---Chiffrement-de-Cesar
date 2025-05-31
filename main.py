#Lancer le Chiffrement de Cesar

from Interface import *
from time import perf_counter


tic = perf_counter()  #Demarrage du chrono
interface()
toc = perf_counter()  #Fin du chrono

print(f"temps d'execution de la fonction brute force : {toc-tic}  [s]")

renouveler = input('Voulez-vous recommencer ? (oui/non):').lower()
if renouveler == "oui":
    interface()
else:
    quit()



