# Bienvenue dans le chiffrement de César 

Ce projet implémente le cryptage et décryptage de mots et phrases que la clefs soit connue ou non. Dans le cas où la clefs n'est pas connue, le programme utilisera la méthode force brute. 

## Fonctionnalités 
- Importe un fichier à crypter ou décrypter
- Importe un fichier contenant les mots les plus courants de la langue française
- Crypte et décrypte des mots ou phrases connaissant la clefs
- Décrypte un mots ou un ensmeble de mots ne connaissant pas la clefs
- Permet une interface utilisateur (choix de clefs, choix sur le chifrement ou dechiffrement, recommencer)

## Prérequis 
- Python 3.7 ou version plus récente
- 'mots_courants.txt' : fichier contenant les mots les plus fréquents de la langues française

## Utilisation 
1) Lancez le programme en appuyant sur 'Run'
2) Choisissez le mode de cryptage ou décryptage 
3) Choisissez d'utiliser votre fichier texte ou entrez un texte dans la console
4) Choisissez le mode clef connue ou non
5) Le programme renvoie le mot ou texte crypter ou décrypter selon le choix de l'utilisateur
6) Vous pouvez décider de recommencer ou vous arrêter 

## Structure du projet 
- 'Cryptage_decryptage.py' : fonctions de chiffrement et déchiffrement
- 'Bruteforce.py' : Déchiffrement sans clef connue
- 'Interface.py' : Interface utilisateur

## Architecture
![image](https://github.com/user-attachments/assets/40aefb74-a500-4003-899b-e132964f45d8)


## Créateurs 
Projet réalisé par : 
[Noé /Morance] 
[Victor /Laloi]
[Elsa /Kupfer] 

## Références 
- https://stackoverflow.com/questions/18982610/difference-between-except-and-except-exception-as-e
- #fonction prise de ilona daumas dans son jeu du pendu corrigé
- https://www.france-ioi.org/algo/course.php?idChapter=595&idCourse=2353#:~:text=La%20fonction%20split%20permet%2C%20%C3%A0,alors%20acc%C3%A9der%20de%20mani%C3%A8re%20classique


