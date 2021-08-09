from tkinter import *
import time

def parpadear():
    '''Aparece e desaparece no intervalo de 3 segundos'''
    ventana.iconify()
    time.sleep(3)
    ventana.deiconify()

ventana = Tk()
ventana.title('Primeira janela em Tkinter')
boton = Button(ventana, text='Evento', command=parpadear)
boton.pack()
ventana.mainloop()