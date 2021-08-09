from tkinter import *

class Janela:
    def __init__(self, raiz):
        self.container1 = Frame(raiz)
        self.container2 = Frame(raiz)
        self.container3 = Frame(raiz)
        self.container1.pack(side=LEFT)
        self.container2.pack(side=RIGHT)
        self.container3.pack(side=TOP)

        self.botao1 = Button(self.container1, text='1')
        self.botao1.pack(side=BOTTOM)

        self.botao2 = Button(self.container1, text='2')
        self.botao2.pack()

        self.botao3 = Button(self.container2, text='3')
        self.botao3.pack(side=TOP)

        self.botao4 = Button(self.container2, text='4')
        self.botao4.pack()

        self.botao5 = Button(self.container3, text='CENTRO')
        self.botao5.pack()


raiz = Tk()
Janela(raiz)
raiz.mainloop()
