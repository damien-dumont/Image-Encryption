import datetime
import rsa
from math import sqrt
import numpy as np
from PIL import Image
import random
import tkinter as tk

root = tk.Tk()
root.title("Encryptor/Decryptor tool V1.0")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, minsize=100, weight=1)

txt_read = tk.Text(root, relief=tk.GROOVE, bd=1, width=50)
left_grid = tk.Frame(root)
right_grid = tk.Frame(root)




def keygen():
        (publicKey, privateKey) = rsa.newkeys(2048)
        publicKeyPEM = publicKey.save_pkcs1().decode()
        privateKeyPEM = privateKey.save_pkcs1().decode()

        with open("private.txt", "w") as f:
                f.write(privateKeyPEM)

        with open("public.txt", "w") as f:
            f.write(publicKeyPEM)






def cypher():
    string = name.get()

    ############ 2.a
    now = datetime.datetime.now()  # Add the date at the beginning of the message

    year = "[" + str(now.year) + "/" + str(now.month) + "/" + str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + "] > "

    string = year + string
    ############ 3
    with open("public.txt", "r") as f:
        publicKeyPEM = f.read()
    publicKey  = rsa.PublicKey.load_pkcs1(publicKeyPEM.encode('utf8'))  # Encryption -> limited to 220 characters because of the date and ID
    encMessage = rsa.encrypt(string.encode(),publicKey)
    ############ 3.a
    ID_w = "     "                       # ID must be multiple of 3, see below

    if len(ID_w)%3 != 0:
        loop = 3-(len(ID_w)%3)
        for i in range(loop):
            ID_w += " "

    ID_ord=[0]*len(ID_w)
    for i in range(len(ID_w)):
        ID_ord[i]=ord(ID_w[i])

    ########### 4
    Msg = list(encMessage)
    Msg = ID_ord + Msg                   # Inputting the ID at the start
    last_byte = int()

    if len(Msg)%3 != 0:                  # Msg size must be multiple of 3, because 3 ints = 1 pixel
        loops = 3-(len(Msg)%3)
        for i in range(loops):
            a = random.randint(0,255)
            Msg += [a]
        last_byte += loops
    print(last_byte)
    ########## 5
    size = len(Msg)/3

    if int(sqrt(size)) == sqrt(size):
        pass
    else:
        Missing = pow(int(sqrt(size)) + 1, 2) - size  # Adding "0" until the number of pixels is a square number
        for i in range((int(Missing)*3)-1):
            a = random.randint(0,255)
            Msg += [a]
        last_byte += (int(Missing)*3)
        Msg += [last_byte]
    ############# 6

    chunks, chunk_size = len(Msg), 3
    split = [ Msg[i:i+chunk_size] for i in range(0, chunks, chunk_size) ] # On split la liste par groupe de 3 pour faire un pixel

    data = np.array(split)        #setup de la matrice
    side = int(sqrt(len(Msg)/3))  #mettre en integer pour les calculs après
    shape = (side,side)         #matrice carrée
    w, h = side, side
    matrix = np.zeros((h, w, 3), dtype=np.uint8)
    for i in range(1,side+1):
        for j in range(1,side+1):
            a = (j-1) + (i-1)*10
            for h in range(1,4):
                matrix[i-1][j-1][h-1] = split[a][h-1]

    img = Image.fromarray(matrix, 'RGB')
    img.save('Output_image2.png')   # all good!





name = tk.StringVar()
txt_write = tk.Entry(root, relief=tk.GROOVE, bd=1, width=60, textvariable=name)




def decypher():
    img = Image.open("Output_image2.png")
    imgArray = np.array(img)

    b = imgArray.flatten()
    b = list(b)
    ID_R = "      "

    if len(ID_R)%3 != 0:
        loop = 3-(len(ID_R)%3)
        for i in range(loop):
            ID_R += " "

    WOID_L = int(len(ID_R))
    WOID = b[WOID_L:]          # Removing ID, as it is not encrypted

    n_removed = int(WOID[-1])   # Reads the number of characters to remove at the end
    for i in range(n_removed):
        WOID = WOID[0:-1]

    WOID_b= bytes(WOID)
    with open("private.txt", "r") as f:
        privateKeyPEM = f.read()

    privateKey  = rsa.PrivateKey.load_pkcs1(privateKeyPEM.encode('utf8'))
    decMessage = rsa.decrypt(WOID_b, privateKey).decode()
    txt_read.insert(tk.END, decMessage)





btn_keygen = tk.Button(left_grid, text="Generate keys", width=30, command=lambda:keygen())
btn_get_image = tk.Button(right_grid, text = "Load encrypted image", width=30)
btn_key_public = tk.Button(left_grid, text="Load public keys file", width=30)
btn_key_private = tk.Button(right_grid, text="Load private keys file", width=30)
btn_key_cypher = tk.Button(left_grid, text = "Encrypt message", width=30, command=lambda:cypher())
btn_key_decypher = tk.Button(right_grid, text = "Decrypt message", width=30, command=lambda:decypher())
write_label = tk.Label(left_grid, text="Write your message here", width=30, bg="black", fg="white")
read_label = tk.Label(right_grid, text="Your message will be displayed here", width=30, bg="black", fg="white")

btn_keygen.grid(row=0, column=0, sticky="ns")
btn_key_public.grid(row=1, column=0, sticky="ns")
btn_get_image.grid(row=0, column=0)
btn_key_private.grid(row=1, column=0, sticky="ns")

left_grid.grid(row = 0, column=0, sticky="ns")
right_grid.grid(row = 0, column=1, sticky="ns")

txt_write.grid(column=0, sticky="nsew", padx=5, pady=5)
txt_read.grid(row=1,column=1, sticky="nsew", padx=5, pady=5)

btn_key_cypher.grid(row=2, column=0, sticky="ns")
btn_key_decypher.grid(row=2, column=0, sticky="ns")
write_label.grid(row=3, sticky="ns")
read_label.grid(row=3, sticky="ns")

root.mainloop()