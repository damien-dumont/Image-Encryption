# Save data from entry widget to a text file:
import tkinter as tk
import os

def save_data():
  name_info = name.get()

  f = open("Input.txt", "w")
  f.write(name_info)
  f.close()

  os.system('python Encryption_code.py')

def decode():
    os.system('python Decryption_code.py')

root = tk.Tk()
root.title("Coder/decoder")
fr_buttons = tk.Frame(root)

name = tk.StringVar()

txt_edit = tk.Entry(root, textvariable=name)
txt_edit.place(height = 100, x = 50, y = 0, width=200)

txt_encode = tk.Button(root, text='Encode', command=lambda:save_data())
txt_encode.place(x = 0, y = 0, width= 50, height=50)

txt_decode = tk.Button(root, text='Decode', command=lambda:decode())
txt_decode.place(x = 0, y = 50, width= 50, height=50)


root.mainloop()