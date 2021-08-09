from tkinter import *

def imprime():
    print('Acabas de pressionar o botao imprimir')

ventana = Tk()
ventana.title('Segunda janela')
botons = Button(ventana, text='Sair',fg='red', command=ventana.quit)
botons.pack(side=LEFT)
botoni = Button(ventana, text='Imprimir',fg='blue', command=imprime)
botoni.pack(side=RIGHT)
ventana.mainloop()