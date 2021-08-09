# Agenda II

from tkinter import *
from tkinter import messagebox

lista = []


def guardar():
    n = nome.get()
    ap = app.get()
    am = apm.get()
    c = coreio.get()
    t = telefone.get()
    lista.append(f'{n}${ap}${am}${t}${c}')
    escrever()
    messagebox.showinfo('Guardado', 'O contacto foi guardado na agenda.')
    nome.set('')
    app.set('')
    apm.set('')
    apm.set('')
    coreio.set('')
    telefone.set('')
    consultar()


def eliminar():
    eliminado = conteliminar.get()
    removido = False
    for elemento in lista:
        arreglo = elemento.split('$')
        if conteliminar.get() == arreglo[3]:
            lista.remove(elemento)
            removido = True
    escrever()
    consultar()
    if removido:
        messagebox.showinfo('Eliminar', f'Elemento eliminado {eliminado}')


def consultar():
    r = Text(ventana, width=80, height=15)
    lista.sort()
    valores = []
    r.insert(INSERT, 'Nome\tApelido P\tApelido M\t\tTelefone\t\tCorreio\n')

    for elemento in lista:
        arreglo = elemento.split('$')
        valores.append(arreglo[3])
        r.insert(INSERT, f'{arreglo[0]}\t{arreglo[1]}\t'
                         f'  {arreglo[2]}\t\t{arreglo[3]}\t\t'
                         f'{arreglo[4]}\t\n')
    r.place(x=20, y=230)
    spinTelefone = Spinbox(ventana, value=(valores),
                           textvariable=conteliminar).place(x=450, y=50)
    if lista == []:
        spinTelefone = Spinbox(ventana, values=(valores),
                               textvariable=conteliminar).place(x=450, y=50)
    r.config(state=DISABLED)


def iniciarArquivo():
    arquivo = open('agenda.txt', 'a')
    arquivo.close()


def carregar():
    arquivo = open('agenda.txt', 'r')
    linha = arquivo.readline()
    if linha:
        while linha:
            if linha[-1] == '\n':
                linha = linha[:-1]
            lista.append(linha)
            linha = arquivo.readline()
    arquivo.close()


def escrever():
    arquivo = open('agenda.txt', 'w')
    lista.sort()
    for elemento in lista:
        arquivo.write(elemento + '\n')
    arquivo.close()


ventana = Tk()
nome = StringVar()
app = StringVar()
apm = StringVar()
coreio = StringVar()
telefone = StringVar()
conteliminar = StringVar()
colorFundo = '#006'
colorLetra = "#fff"
ventana.title('Agenda com arquivos')
ventana.geometry('700x500')
ventana.configure(background=colorFundo)
etiquetaTitulo = Label(ventana, text='Agenda com arquivos',
                       bg=colorFundo, fg=colorLetra).place(x=270, y=10)
etiquetaN = Label(ventana, text='Nome', bg=colorFundo, fg=colorLetra
                  ).place(x=50, y=50)
caixaN = Entry(ventana, textvariable=nome).place(x=150, y=50)
etiquetaApp = Label(ventana, text='Apelido Paterno',
                    bg=colorFundo, fg=colorLetra).place(x=50, y=80)
caixaApp = Entry(ventana, textvariable=app).place(x=150, y=80)
etiquetaApm = Label(ventana, text='Apelido Materno',
                    bg=colorFundo, fg=colorLetra).place(x=50, y=110)
caixaApm = Entry(ventana, textvariable=apm).place(x=150, y=110)
etiquetaT = Label(ventana, text='Telefone',
                      bg=colorFundo, fg=colorLetra).place(x=50, y=140)
caixaT = Entry(ventana, textvariable=telefone).place(x=150, y=140)
etiquetaC = Label(ventana, text='Correo', bg=colorFundo,
                  fg=colorLetra).place(x=50, y=170)
caixaC = Entry(ventana, textvariable=coreio).place(x=150, y=170)
etiquetaEliminar = Label(ventana, text='Telfone',
                         bg=colorFundo, fg=colorLetra).place(x=370, y=50)
spinTelefone = Spinbox(ventana, textvariable=conteliminar).place(x=450, y=50)
botaoGuardar = Button(ventana, text='Guardar', command=guardar,
                      bg='#009', fg='white').place(x=180, y=200)
botaoEliminar = Button(ventana, text='Eliminar', command=eliminar,
                       bg='#009', fg='white').place(x=490, y=80)
mainloop()
