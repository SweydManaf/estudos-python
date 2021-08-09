from tkinter import *

master = Tk()
master.title("Titulo")
master.geometry('500x500')

label1 = Label(master,
               text='frase de teste\nteste',
               font='Arial 20',
               bd=1,
               relief='solid',
               width=30,
               height=5,
               justify=LEFT,
               anchor=NW,
               padx=5,
               pady=5).pack()


master.mainloop()
