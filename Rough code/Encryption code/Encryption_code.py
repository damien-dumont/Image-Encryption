from array import array
import binascii
from typing import List
import numpy as np
from PIL import Image
from PIL import ImageColor
from math import sqrt
from math import pow
from os import system

with open('Input.txt', 'r') as fichier: #prendre texte
    texte = fichier.readlines() #texte -> liste    ajouter date?

def listToString(texte) :   # liste -> string
    str1 = ""

    for ele in texte:
        str1 += ele
    return str1 

import datetime
now = datetime.datetime.now()

year = "[" + str(now.year) + "/" + str(now.month) + "/" + str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + "] > "

string = listToString(texte) 
string = year + string
encodé = string.encode("ascii")  # string -> bytes
hexa = binascii.hexlify(encodé)  # convertir en hexa decimal pour connaitre la taille si c est multiple de 6

if len(hexa) % 6 == 0:    # si c est un multiple de 6: cool!
    pass
else:
    nbr_de_0 = 6 - len(hexa) % 6   # si c est pas un multiple de 6:
    oui = int(nbr_de_0 / 2)   # combien d'espaces à rajouter pour devenir un multiple de 6?
    for i in range(oui):      #je rajoute des espaces à string? encodé? pour devenir un multiple de 6
        espace = " "
        string += espace

Length = len(hexa) / 6
if int(sqrt(Length)) == sqrt(Length):     # besoin que la matrice d hex soit carrée pour faire une image plus tard
    pass
else:
    Missing = pow(int(sqrt(Length)) + 1, 2) - Length  # Il me manque "missing" groupes de 6 pour avoir un carré
    # Espaces à rajouter = nbre de groupe de 6 manquants / 3 (puisque chaque caractère donne 2 hexadec)
    for i in range(int(Missing)):
        espace = "   "
        string += espace

encodé = string.encode("ascii")  # string -> bytes
hexa = binascii.hexlify(encodé)  # convertir en hexa decimal pour connaitre la taille si c est multiple de 6

# Hexa est notre code hexadécimal, dont la longueur est un multiple de 6



#  hexadécimal -> couleurs et image (carré!)

hexad = hexa.decode("ascii") #on a le hexadecimal sous forme de string, ce qui facilite le travail comparé à bytes
chunks, chunk_size = len(hexad), 6
yes = [ hexad[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
data = np.array(yes)        #setup de la matrice
coté = int(sqrt(len(yes)))  #mettre en integer pour les calculs après
shape = (coté,coté)         #matrice carrée
matrix = data.reshape(shape)#matrice créée

w, h = coté, coté
hello = np.zeros((h, w, 3), dtype=np.uint8)  # hello est la matrice mais avec les couleurs en RGB, on la setup ici

for i in range(coté):
    for j in range(coté):
        a = matrix[i-1, j-1]
        n = 2	# every 2 characters
        split_string = [a[k:k+n] for k in range(0, len(a), n)]
        for h in range(3):
            z = int(split_string[h],16)
            hello[i-1, j-1, h] = z
print(hello)
img = Image.fromarray(hello, 'RGB')
img.save('Output_image.png')

