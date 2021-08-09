from tkinter import *

master = Tk()
master.title("Titulo")
master.geometry('500x500')

border = 4


label1 = Label(master,
               text="solid",
               font='Arial 20',
               bd=border,
               relief='solid' # mais frequente
               ).pack()

label2 = Label(master,
               text="flat",
               font='Arial 20',
               bd=border,
               relief='flat' # liso
               ).pack()

label3 = Label(master,
               text="raised",
               font='Arial 20',
               bd=border,
               relief='raised' # para cima
               ).pack()

label4 = Label(master,
               text="sunken",
               font='Arial 20',
               bd=border,
               relief='sunken' # afundado
               ).pack()

label5 = Label(master,
               text="ridge",
               font='Arial 20',
               bd=border,
               relief='ridge' #
               ).pack()

label6 = Label(master,
               text="groove",
               font='Arial 20',
               bd=border,
               relief='groove'
               ).pack()

master.mainloop()
