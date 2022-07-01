# importation de tous les modules
import os, time
from colorama import Back, Fore, Style, deinit, init
import random

#Def pour le changement de couleur automatique
names = [Fore.BLUE + Fore.RED + Style.BRIGHT, Fore.MAGENTA + Style.BRIGHT, Fore.CYAN + Style.BRIGHT,
         Fore.GREEN + Style.BRIGHT, Fore.WHITE + Style.BRIGHT, Fore.YELLOW + Style.BRIGHT]


def selectRandom(names):
    return random.choice(names)

# Endroit ou il faut mettre le nom des frames choisis
os.system('cls')
filenames = ["Name.files.txt"]
frames = []

# variable pour la boucle while infinie
x = 1

# Print le choix de couleurs
print("Here are all the colours available  :\n"
      "\t- Rouge = 1    - Jaune  = 4\n"
      "\t- Bleu  = 2    - Violet = 5\n"
      "\t- Vert  = 3    - RGB    = 6\n")

#Demander à choisir la couleur
color = input("Choose color : ")

#Variable pour toutes les couleurs
red = str(1)
blue = str(2)
green = str(3)
yellow = str(4)
magenta = str(5)
RGB = str(6)

#Début de la boucle while infine

while x > 0:

#Premiere condition pour savoir quelles couleurs choisir
    if color == red:
        for name in filenames:
            with open(name,"r",encoding="utf8") as f:
                frames.append(f.readlines())

        for frame in frames:
            print(Fore.RED + "".join(frame))
            time.sleep(0.2)
            os.system('cls')

    elif color == blue:
        for name in filenames:
            with open(name,"r",encoding="utf8") as f:
                frames.append(f.readlines())

        for frame in frames:
            print(Fore.BLUE + "".join(frame))
            time.sleep(0.2)
            os.system('cls')

    elif color == green:
        for name in filenames:
            with open(name,"r",encoding="utf8") as f:
                frames.append(f.readlines())

        for frame in frames:
            print(Fore.GREEN + "".join(frame))
            time.sleep(0.2)
            os.system('cls')

    elif color == yellow:
        for name in filenames:
            with open(name,"r",encoding="utf8") as f:
                frames.append(f.readlines())

        for frame in frames:
            print(Fore.YELLOW + "".join(frame))
            time.sleep(0.2)
            os.system('cls')

    elif color == magenta:
        for name in filenames:
            with open(name,"r",encoding="utf8") as f:
                frames.append(f.readlines())

        for frame in frames:
            print(Fore.MAGENTA + "".join(frame))
            time.sleep(0.2)
            os.system('cls')

    elif color == RGB:
        for name in filenames:
            with open(name,"r",encoding="utf8") as f:
                frames.append(f.readlines())

        for frame in frames:
            print(selectRandom(names) + "".join(frame))
            time.sleep(0.2)
            os.system('cls')