from tkinter import *
from tkinter import ttk

master = Tk()

lista = Listbox(master, selectmode=EXTENDED)
lista.pack()

# Inserir um item de cada vez
# lista.insert(END, 'Primeiro item da lista')
# lista.insert(END, 'Segundo item da lista')
# lista.insert(END, 'Terceiro item da lista')
# lista.insert(END, 'Quarto item da lista')

# Inserir varios item a partir de uma list
nomes = ['Sweyd', 'Joao', 'Ana', 'Telvio']
for nome in nomes:
    lista.insert(END, nome)

lista.delete(1, 1) # indice do valor

def executar():
    print(lista.get(ACTIVE))

btn = Button(master, text='Clique', command=executar).pack()


# Alguns eventos do listbox
# lbox.bind('<<ListboxSelect>>', showPopulation)
# lbox.bind('<Double-1>', sendGift)
# root.bind('<Return>', sendGift


master.mainloop()