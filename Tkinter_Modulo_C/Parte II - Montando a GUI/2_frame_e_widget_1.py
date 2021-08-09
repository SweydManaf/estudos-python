from tkinter import *

class Janela:
    def __init__(self, toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text='Oi!', bg='green')
        self.botao.pack()

        """
        Configuracoes do Button:
            height - serve para configurar qual a altura do botao
            width - especifica a largura do botao
            font - configura a fonte atraves 
                de uma tupla ("tipo de fonte", "tamanho", "negrito", "italico")
            fg - configura a cor do texto."""

raiz = Tk()
Janela(raiz)
raiz.mainloop()
