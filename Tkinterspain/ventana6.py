# ventana 6: SpinBox

from tkinter import *

def obter():
    print(valor.get())

ventana = Tk()
valor = StringVar()
ventana.title('Uso de spinbox com tkinter')
ventana.geometry('400x300')
etiqueta = Label(ventana, text='Exemplo 1 de spinbox').place(x=20, y=20)
combo = Spinbox(ventana, values=('Um', 'Dois', 'Treis',
                                 'Quatro', 'Cinco')).place(x=20, y=50)
etiqueta2 = Label(ventana, text='Exemplo 2 de SpinBox').place(x=20, y=80)
combo2 = Spinbox(ventana, from_=1, to=10,textvariable=valor).place(x=20, y=110)
botton = Button(ventana, text='Obter valor SpinBox', command=obter).place(x=80, y=140)
mainloop()