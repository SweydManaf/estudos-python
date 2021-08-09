from tkinter import *
from tkinter import ttk


master = Tk()
nome = StringVar()


def executar():
    NOME = nome.get()
    etiqueta_name = Label(master, text=f'O teu nome e {NOME}')
    etiqueta_name.grid()

etiqueta_nome = Label(master, text='O teu nome')
caixa_nome = Entry(master, textvariable=nome)
btn_executar = Button(master, text='Executar', command=executar)

etiqueta_nome.grid(row=0, column=0)
caixa_nome.grid(row=1, column=0)
btn_executar.grid(columnspan=3, pady=10)

caixa_nome.focus_force()

master.mainloop()