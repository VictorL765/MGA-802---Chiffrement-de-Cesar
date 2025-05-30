# Evaluation du temps de calul pour la fonction brute force

from time import perf_counter
from Bruteforce import brute_force

#Fonction qui evalue le temps d'execution de la methode brute force
def performance_brute_force(texte):
    tic = perf_counter()  #Demarrage du chrono
    brute_force(texte)
    toc = perf_counter()  #Fin du chrono

    #Affichage du temps d'execution en seconde
    print(f"temps d'execution de la fonction brute force : {toc-tic}  [s]")



