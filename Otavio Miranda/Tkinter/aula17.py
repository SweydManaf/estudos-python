from tkinter import *

# grid manager

master = Tk()
master.title('Titulo')
#master.geometry('500x500')

label1 = Label(master,
               text='label 1',
               font='Arial 20',
               bg='red')

label2 = Label(master,
               text='label 2',
               font='Arial 20',
               bg='green')

label3 = Label(master,
               text='label 2',
               font='Arial 20',
               bg='blue')
btn1 = Button(master, text='Click 1')
btn2 = Button(master, text='Click 2')
btn3 = Button(master, text='Click 3')

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)

master.mainloop()