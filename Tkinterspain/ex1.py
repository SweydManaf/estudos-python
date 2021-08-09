from tkinter import *

def saudacao():
    print('Ola todos!')

janela = Tk()
janela.title('Exercicio numero 1')
janela.geometry('400x200')
etiqueta1 = Label(janela, text='Saudacao').place(x=30, y=50)
boton = Button(janela, text='Clica para saudar', command=saudacao).place(x=200, y=50)
etiqueta2 = Label(janela, text='Minimizar').place(x=30, y=100)
boton2 = Button(janela, text='Clique para minimizar', command=janela.iconify).place(x=200, y=100)
janela.mainloop()
