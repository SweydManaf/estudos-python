from tkinter import *

master = Tk()
master.title("Titulo")
master.geometry("500x300")

label1 = Label(master,
               text='Este e o meu label',
               font='Arial')

label2 = Label(master,
               text='Este e o meu label 2',
               font='Arial 20 italic')

label3 = Label(master,
               text='Este e o meu label 3',
               font='Verdana 32 bold',
               fg='gray')

label1.pack()
label2.pack()
label3.pack()
master.mainloop()
