#Ce module sert à intégrer les fichiers textes dans le programme

import os

#On va ici aussi standariser l'affichage
def afficher(message):
    print(message)


#lire le contenue d'un fichier texte
def lire_fichier(nom_fichier):


   # teste si le fichier existe
   full_filename = os.path.join(nom_fichier)
   if not os.path.isfile(full_filename):
       raise RuntimeError(f'Je ne trouve pas le fichier {full_filename} !')

   # Ouvre le fichier contenant les mots en mode lecture
   with open(full_filename, 'r', encoding='utf8') as f:
       # Lire le contenu du fichier
       contenu = f.read()
   return contenu




