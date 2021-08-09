from tkinter import *

def operation():
    numero = num.get()
    if option.get() == 2:
        total = numero * 10
    elif option.get() == 3:
        total = numero * 30
    elif option.get() == 4:
        total = numero * 40
    elif option.get() == 50:
        total = numero * 50
    else:
        total = numero * numero
    print(f'O total da operacao e: {str(total)}')

ventana = Tk()
option = IntVar()
num = IntVar()
ventana.title('Radio Botao em tkinter')
ventana.geometry('400x300')
etiqueta1 = Label(ventana, text='Escreve o numero: ').place(x=20, y=20)
caixa_nome = Entry(ventana, textvariable=num).place(x=130, y=20)
etiqueta2 = Label(ventana, text='Escreva tua opcao: ').place(x=20, y=50)
x10 = Radiobutton(ventana, text='X10', value=1, variable=option).place(x=20, y=80)
x20 = Radiobutton(ventana, text='X20', value=2, variable=option).place(x=70, y=80)
x30 = Radiobutton(ventana, text='X30', value=3, variable=option).place(x=120, y=80)
x40 = Radiobutton(ventana, text='X40', value=4, variable=option).place(x=20, y=110)
x50 = Radiobutton(ventana, text='X50', value=5, variable=option).place(x=70, y=110)
quadrado = Radiobutton(ventana, text='Quadrado', value=6, variable=option).place(x=120, y=110)
boton = Button(ventana, text='Realiza operacao', command=operation).place(x=20, y=140)
ventana.mainloop()
