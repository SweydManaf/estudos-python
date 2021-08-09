# Posicionamentos

from tkinter import *

ventana = Tk()
ventana.title('Posicionamentos')
ventana.geometry('400x200')
boton = Button(ventana, text='Posicionamento diferente').place(x=10, y=10)
etiqueta = Label(ventana, text='Posicionamento diferente').place(x=200, y=10)
etiqueta1 = Label(ventana, text='Posicionamento diferente 2').place(x=10, y=30)
etiqueta3 = Label(ventana, text='Posicionamento 3').place(x=200, y=30)
ventana.mainloop()