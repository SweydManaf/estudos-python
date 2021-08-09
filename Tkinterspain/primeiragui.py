from tkinter import *

ventana = Tk()
ventana.title('MEU PRIMEIRO APP GUI')
boton = Button(ventana, text='Minimizar', command=ventana.iconify)
boton.pack()
etiqueta = Label(ventana, text='Ola Mundo em Python')
etiqueta.pack()
etiqueta.mainloop()