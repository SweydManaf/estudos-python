from tkinter import *

master = Tk()

def verificar():
    print(valor_check.get())

valor_check = IntVar()
check = Checkbutton(master,
                    text='Deseja colocar na area de trabalho',
                    variable=valor_check,
                    command=verificar).pack()

master.mainloop()