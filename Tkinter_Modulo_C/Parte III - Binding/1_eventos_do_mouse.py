from tkinter import *

class Janela:
    def __init__(self, raiz):

        # Cria o espaco no topo da tela tela
        self.frame = Frame(raiz)
        self.frame.pack()

        # Cria um rotulo com texto
        self.texto = Label(self.frame, text='Clique para ficar amarelo')
        self.texto['width'] = 26
        self.texto['height'] = 3
        self.texto.pack()

        # Cria um botao verde na tela
        self.botaoverde = Button(self.frame, text='Clique')
        self.botaoverde['bg'] = 'green'
        self.botaoverde.bind("<Double-Button-1>", self.muda_cor)
        #self.botaoverde.focus_force()
        self.botaoverde.pack()

    def muda_cor(self, event):
        # Muda a cor do botao
        if self.botaoverde['bg'] == 'green':
            self.botaoverde['bg'] = 'yellow'
            self.texto['text'] = 'Clique para ficar verde'
        else:
            self.botaoverde['bg'] = 'green'
            self.texto['text'] = 'Clique para ficar amarelo'

raiz = Tk()
Janela(raiz)
raiz.mainloop()


