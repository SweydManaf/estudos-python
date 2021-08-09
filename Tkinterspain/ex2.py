from tkinter import *
from tkinter import messagebox

lista = []

def guardar():
    t = titulo.get()
    a = autor.get()
    e = editora.get()
    p = paginas.get()
    l = limite.get()
    lista.append(f'{t}${a}${e}${p}${l}')
    escrever()
    messagebox.showinfo('Guardado', 'O livro foi armazenado')
    titulo.set('')
    autor.set('')
    editora.set('')
    paginas.set('')
    limite.set('')
    consultar()

def eliminar():
    temp = lista[0].split('$')
    temp = temp[0]
    if messagebox.askyesno(f'Eliminar livro',
                        f'Deseja eliminar o livro com titulo:\n{temp}'):
        eliminado = conteliminar.get()
        removido = False
        for elemento in lista:
            arreglo = elemento.split('$')
            if conteliminar.get() == arreglo[0]:
                lista.remove(elemento)
                removido = True
        escrever()
        consultar()
        if removido:
            messagebox.showinfo('Eliminar', f'Voce eliminou o livro com'
                                            f'o titulo {eliminado}')

def consultar():
    r = Text(janela, width=80, height=14)
    lista.sort()
    valores = []
    r.insert(INSERT, '\t\tTitulo do livro\n')
    r.insert(INSERT, '-' * 80)
    for elemento in lista:
        arranjo = elemento.split('$')
        valores.append(arranjo[0])
        r.insert(INSERT, f'\n\t\t{arranjo[0]}\n')
        r.insert(INSERT, f'Autor: {arranjo[1]}'
                         f' No de paginas: {arranjo[2]}'
                         f' Fecha limite: {arranjo[3]}\n')
        r.insert(INSERT, '-' * 80)
        r.insert(INSERT, '')
    r.place(x=30, y=210)
    spinLivro = Spinbox(janela, values=valores,
                        textvariable=conteliminar).place(x=40, y=450, width=450)
    butaoeliminar = Button(janela, text='Livro lido', command=eliminar,
                           bg='#009', fg='white').place(x=500, y=450, width=100)
    if lista == []:
        spinLivro = Spinbox(janela, values=valores).place(x=40,y=450, width=450)
    r.config(state=DISABLED)


def iniciarArquivo():
    arquivo = open('livros.txt', 'a')
    arquivo.close()


def carregar():
    arquivo = open('livros.txt', 'r')
    linha = arquivo.readline()
    if linha:
        while linha:
            if linha[-1] == '\n':
                linha = linha[:-1]
            lista.append(linha)
            linha = arquivo.readline()
        arquivo.close()


def escrever():
    arquivo = open('livros.txt', 'w')
    for elemento in lista:
        arquivo.write(elemento + '\n')
    arquivo.close()

janela = Tk()
titulo = StringVar()
autor = StringVar()
editora = StringVar()
paginas = StringVar()
limite = StringVar()
conteliminar = StringVar()
colorFundo = '#006'
colorLetra = "#fff"
janela.title('Relacao de livros que tenho que ler')
janela.geometry('700x500')
janela.configure(background=colorFundo)
etiquetaTitulo = Label(janela, text='Relacao de livros que tenho que ler',
                       bg=colorFundo, fg=colorLetra).place(x=270, y=10)
etiquetaT = Label(janela, text='Titulo', bg=colorFundo, fg=colorLetra,
                  ).place(x=50, y=50)
caixaT = Entry(janela, textvariable=titulo).place(x=150, y=50, width=400)
botaoT = Button(janela, text='Aumentar livro', command=guardar,
                bg='#009', fg='white').place(x=560, y=50)
etiquetaA = Label(janela, text='Autor', bg=colorFundo,
                  fg=colorLetra).place(x=50, y=80)
caixaA = Entry(janela, textvariable=autor).place(x=150, y=80)
etiquetaE = Label(janela, text='Editora', bg=colorFundo,
                  fg=colorLetra).place(x=50,y=110)
caixaE = Entry(janela, textvariable=editora).place(x=150, y=110)
etiquetaP = Label(janela, text='No de paginas', bg=colorFundo,
                  fg=colorLetra).place(x=50, y=140)
caixaP = Entry(janela, textvariable=paginas).place(x=150, y=140)
etiquetaL = Label(janela, text='Fecha limite', bg=colorFundo,
                  fg=colorLetra).place(x=50, y=170)
caixaL = Entry(janela, textvariable=limite).place(x=150, y=170)


mainloop()