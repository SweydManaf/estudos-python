from tkinter import *

class janela:
    def __init__(self, raiz):
        self.frame1 = Frame(raiz)
        self.frame1.pack()

        self.frame2 = Frame(raiz)
        self.frame2.pack()

        self.titulo = Label(self.frame1, text='ANALISA EVENTOS',
                            font=('Verdana', '13', 'bold'))
        #self.titulo.focus_force()
        self.titulo.pack()

        self.botao1 = Button(self.frame2, text='Botao 1')
        self.botao1['padx'], self.botao1['pady'] = 10, 5
        self.botao1['bg'] = 'red'
        self.botao1['fg'] = 'green'
        self.botao1['relief'] = GROOVE
        self.botao1.bind('<Motion>', self.pinta_b1)
        self.botao1.bind('<Leave>', self.repinta_b1)
        self.botao1.pack()

    def pinta_b1(self, event): self.botao1['bg'] = 'yellow'
    def repinta_b1(self, event): self.botao1['bg'] = 'red'



raiz = Tk()
janela(raiz)
raiz.mainloop()