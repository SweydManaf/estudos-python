# Agenda I

from tkinter import *
from tkinter import messagebox

lista = []

def guardar():
    print('Ola')


def eliminar():
    print('Ola')


ventana = Tk()
nome =  StringVar()
app = StringVar()
apm = StringVar()
coreio = StringVar()
telefone = StringVar()
conteliminar = StringVar()
colorFundo = '#006'
colorLetra = "#fff"
ventana.title('Agenda com arquivos')
ventana.geometry('700x500')
ventana.configure(background = colorFundo)
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