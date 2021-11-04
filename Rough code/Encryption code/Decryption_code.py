import numpy as np
from PIL import Image
import binascii

img = Image.open("Output_image.png")
imgArray = np.array(img)

coté = int(imgArray.shape[1])
w, h = coté, coté
matrix = np.zeros((w, h), dtype = list)

for i in range(coté):
    for j in range(coté):
        a = imgArray[i-1,j-1]
        b = hex(int(a[0]))[2:] + hex(int(a[1]))[2:] + hex(int(a[2]))[2:]
        matrix[i-1, j-1] = b
lister = list()
for i in range(coté):
    lister += matrix.tolist()[i]
def listToString(lister) :   # liste -> string
    str1 = ""

    for ele in lister:
        str1 += ele
    return str1 

hexa = listToString(lister)
encodé = binascii.unhexlify(hexa)
décodé = encodé.decode("ascii")
with open("output.txt", "w") as f:
    f.write(décodé)