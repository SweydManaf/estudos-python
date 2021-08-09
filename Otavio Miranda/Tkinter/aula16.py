from tkinter import *

master = Tk()
master.title('Titulo')
master.geometry('500x500')

texto = StringVar()
texto.set('Novo texto')

label1 = Label(master,
               textvariable=texto,
               font='Arial 20',
               bg='red',
               fg='white')

texto.set('joao')

label1.pack()



master.mainloop()