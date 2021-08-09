from tkinter import *

raiz = Tk()
raiz.title("Title")
raiz.geometry("500x300")


def cmd_Click(mensagem):
    print(mensagem)


# botao
cmd1 = Button(raiz, text='Executar',
             command=lambda :cmd_Click("Nova mensagem"))
cmd1.pack()

cmd2 = Button(raiz, text='Clicar',
             command=lambda :print('OK'))
cmd2.pack()

raiz.mainloop()
