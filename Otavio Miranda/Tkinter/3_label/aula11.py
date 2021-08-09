from tkinter import *

master = Tk()
master.title("Titulo")

label1 = Label(master, text='Este e o label 1',
               font='Arial 20',
               width=20,
               bg='red')

label2 = Label(master, text='Este e o label 2',
               font='Arial 40',
               width=20,
               bg='red')

label1.pack()
label2.pack()
master.mainloop()
