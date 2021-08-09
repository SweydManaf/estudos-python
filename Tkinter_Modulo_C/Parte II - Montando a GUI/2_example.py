from tkinter import *

class Janela:
    def __init__(self, raiz):
        self.fr1 = Frame(raiz)
        self.fr1.pack()

        self.botao_1 = Button(self.fr1, text='Atacar', bg='blue', fg='green')
        self.botao_1['width'] = 10
        self.botao_1.pack()

        self.botao_2 = Button(self.fr1, text='Defender', bg='white', fg='red')
        self.botao_2['width'] = 10
        self.botao_2.pack()

        self.botao_3 = Button(self.fr1, text='Rematar', bg='yellow', fg='black')
        self.botao_3['width'] = 10
        self.botao_3.pack()


raiz = Tk()
Janela(raiz)
raiz.mainloop()