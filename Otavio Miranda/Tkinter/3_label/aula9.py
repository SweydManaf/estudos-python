from tkinter import *

raiz = Tk()
raiz.title("Titulo")

label_1 = Label(raiz, text="Este e o label 1.")
label_2 = Label(raiz, text="Este e o label 2.")

btn = Button(raiz, text='Executar')

# pack
btn.pack()
label_2.pack()
label_1.pack()

raiz.mainloop()