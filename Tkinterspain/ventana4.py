from tkinter import *

def saudar():
    print(f'Ola {nome.get()} {apelidoP.get()} {apelidoM.get()}')

ventana = Tk()
nome = StringVar()
apelidoP = StringVar()
apelidoM = StringVar()
idade = IntVar
sexo = BooleanVar
nome.set('Escreve teu nome')
ventana.title('Entradas em Tkinter')
ventana.geometry('400x400')
etiqueta1 = Label(ventana, text='Escreve teu nome: ').place(x=10, y=10)
caixa_nome = Entry(ventana, textvariable=nome).place(x=170, y=10)
etiqueta2 = Label(ventana, text='Escreve teu apelito Paterno: ').place(x=10, y=40)
caixa_apelidoP = Entry(ventana, textvariable=apelidoP).place(x=170, y=40)
etiqueta3 = Label(ventana, text='Escreve teu apelido Materno: ').place(x=10, y=70)
caixa_apelidoM = Entry(ventana, textvariable=apelidoM).place(x=170, y=70)
etiqueta4 = Label(ventana, text='Idade: ').place(x=10, y=100)
caixa_idade = Entry(ventana, textvariable=idade).place(x=50, y=100)
etiqueta5 = Label(ventana, text='Sexo: ').place(x=10, y=130)
caixa_sexo = Entry(ventana, textvariable=sexo).place(x=50, y=130)
boton = Button(ventana, text='Saudacao personalizada', command=saudar).place(x=10, y=160)
ventana.mainloop()