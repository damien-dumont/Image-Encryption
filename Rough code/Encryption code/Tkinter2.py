import tkinter as tk
import os

def save_data():
  name_info = name.get()

  f = open("Input.txt", "w")
  f.write(name_info)
  f.close()

  os.system('python Encryption_code.py')
  os.remove("Input.txt")

root = tk.Tk()
root.title("Coder/decoder")
fr_buttons = tk.Frame(root)
root.minsize(width = 350, height = 200)

name = tk.StringVar()

txt_edit = tk.Entry(root, textvariable=name)
txt_edit.place(height = 100, x = 50, y = 0, width=300)

T = tk.Text(root, width=37, height=6)
T.place(x = 50, y = 100)


def decode():
  os.system('python Decryption_code.py')
  with open('output.txt', 'r') as f: #prendre texte
    texte = f.readlines() #texte -> liste    ajouter date?

  def listToString(texte) :   # liste -> string
    str1 = ""

    for ele in texte:
        str1 += ele
    return str1 
  string = listToString(texte)
  T.insert(tk.END, string)
  os.remove("output.txt")

txt_encode = tk.Button(root, text='Encode', command=lambda:save_data())
txt_encode.place(x = 0, y = 0, width= 50, height=100)

txt_decode = tk.Button(root, text='Decode', command=lambda:decode())
txt_decode.place(x = 0, y = 100, width= 50, height=100)


root.mainloop()