from tkinter import *

class Passwords:

    def __init__(self, raiz):
        self.frame1 = Frame(raiz)
        self.frame1.pack()
        self.frame2 = Frame(raiz)
        self.frame2.pack()
        self.frame3 = Frame(raiz)
        self.frame3.pack()
        self.frame4 = Frame(raiz, pady=10)
        self.frame4.pack()

        # Titulo na janela
        Label(self.frame1, text='PASSWORDS', fg='darkblue',
              font=('Verdana', '14', 'bold'), height=3).pack()

        fonte1 = ('Verdana', '10', 'bold')


        # Obtem o nome do usuario
        Label(self.frame2, text='Nome: ',
              font=fonte1, width=8, height=3).pack(side=LEFT)

        self.nome = Entry(self.frame2, width=10, font=fonte1)
        self.nome.insert(END, 'username')
        self.nome.focus_force()
        self.nome.bind('<Down>', self.baixa)
        self.nome.bind('<Key>', self.key)
        self.nome.pack(side=LEFT)

        # Obtem a senha do usuario
        Label(self.frame3, text='Senha: ',
              font=fonte1, width=8).pack(side=LEFT)

        self.senha = Entry(self.frame3, width=10, show='*',
                           font=fonte1)
        self.senha.bind('<Up>', self.cima)
        self.senha.bind('<Return>', self.verifica)
        self.senha.pack(side=LEFT)

        self.confere = Button(self.frame4, font=fonte1, text='Conferir',
                              bg='pink', command=self.conferir)
        self.confere['relief'] = GROOVE
        self.confere.pack()

        # Informacao de acesso
        self.msg = Label(self.frame4, font=fonte1)
        self.msg.pack()


    def conferir(self):
        NOME = self.nome.get()
        SENHA = self.senha.get()
        if NOME != '' and NOME == SENHA:
            self.msg['text'] = 'ACESSO PERMITIDO'
            self.msg['fg'] = 'darkgreen'
        else:
            self.msg['text'] = 'ACESSO NEGADO'
            self.msg['fg'] = 'red'
            self.senha['text'] = ''
            self.nome.focus_force()

    def baixa(self, event): self.senha.focus_force()
    def cima(self, event): self.nome.focus_force()
    def verifica(self, event): self.conferir()
    def key(self, event): self.nome.delete(0, END)

raiz = Tk()
Passwords(raiz)
raiz.mainloop()
