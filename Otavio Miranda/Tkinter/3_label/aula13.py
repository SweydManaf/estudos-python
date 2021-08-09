from tkinter import *

master = Tk()
master.title("Titulo")
master.geometry('500x500')

label1 = Label(master,
               text='0123456789',
               font='Arial 20',
               width=25,
               height=4,
               anchor=CENTER, # pontos cardiais
               bd=1,
               relief='solid').pack()

master.mainloop()
