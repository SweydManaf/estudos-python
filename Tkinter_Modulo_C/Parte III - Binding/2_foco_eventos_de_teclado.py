from tkinter import *

class Janela:
    def __init__(self, raiz):
        self.frame = Frame(raiz)
        self.frame.pack()

        self.frame2 = Frame(raiz)
        self.frame2.pack()

        self.titulo = Label(self.frame, text='VIDENTE 2005',
                            font=('Verdana', '13', 'bold'))
        self.titulo.pack()

        self.msg = Label(self.frame, width=40, height=6,
                         text='Advinhando o evento ocorrido!')
        self.msg.focus_force()
        self.msg.pack()

        # Definindo o botao 1
        self.b01 = Button(self.frame2, text='Botao 1')
        self.b01['padx'], self.b01['pady'] = 10, 5  # espacamento
        self.b01['bg'] = 'deepskyblue'
        self.b01.bind("<Return>", self.keypress01)
        self.b01.bind("<Any-Button>", self.button01)
        self.b01.bind("<FocusIn>", self.fin01)
        self.b01.bind("<FocusOut>", self.fout01)
        self.b01.bind("<Delete>", self.delb01)
        self.b01['relief'] = FLAT
        self.b01.pack(side=LEFT)

        # Definindo botao 2
        self.b02 = Button(self.frame2, text='Botao 2')
        self.b02['padx'], self.b02['pady'] = 10, 5
        self.b02['bg'] = 'deepskyblue'
        self.b02.bind("<Return>", self.keypress02)
        self.b02.bind("<Any-Button>", self.button02)
        self.b02.bind("<ButtonRelease-1>", self.mousedireitob02)
        self.b02.bind("<FocusIn>", self.fin02)
        self.b02.bind("<FocusOut>", self.fout02)
        self.b02['relief'] = RIDGE
        self.b02.pack(side=LEFT)


    def keypress01(self, event): self.msg['text'] = 'ENTER sobre o Botao 1'
    def keypress02(self, event): self.msg['text'] = 'ENTER sobre o Botao 2'

    def button01(self, event): self.msg['text'] = 'Clique sobre o Botao 1'
    def button02(self, event): self.msg['text'] = 'Clique sobre o botao 2'

    def fin01(self, event): self.b01['relief'] = FLAT
    def fout01(self, event): self.b01['relief'] = RIDGE

    def fin02(self, event): self.b02['relief'] = FLAT
    def fout02(self, event): self.b02['relief'] = RIDGE

    def delb01(self, event): self.msg['text'] = 'Delete no botao 1'
    def mousedireitob02(self, event): self.msg['text'] = 'Mouse direito botao 2'

raiz = Tk()
Janela(raiz)
raiz.mainloop()
