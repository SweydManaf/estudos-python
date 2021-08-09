from tkinter import *

# grid manager

root = Tk()
root.title('Login')

label = Label(root, text='Usuario: ')
label.grid(row=0, column=0, stick=W)
texto_usuario = Entry(root).grid(row=0, column=1)

label = Label(root,text='Senha: ')
label.grid(row=1, column=0, stick=W)
texto_senha = Entry(root).grid(row=1, column=1)

btn_login = Button(root, text='Login').grid(row=2, column=1, stick=E)

root.mainloop()
