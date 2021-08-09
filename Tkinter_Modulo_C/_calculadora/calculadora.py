import tkinter as tk
from tkinter import ttk

class Calculadora:
    """Representa uma calculadora."""

    def __init__(self, raiz):
        """Inicializa a calculadora."""

        # Frame 1 campo de texto e resultado
        self.frame1 = tk.Frame(raiz)
        self.frame1.pack()

        # Resultado
        self.caixa_resultado = tk.Entry(self.frame1, width=30, font=(20))
        self.caixa_resultado.focus_force()
        self.caixa_resultado.pack()


        # Frame 2 campos dos numeros e operacoes
        self.frame2 = tk.Frame(raiz)
        self.frame2.pack(side=tk.TOP)

        self.linha1 = tk.Frame(self.frame2)
        self.linha1.pack(side=tk.LEFT)
        self.linha2 = tk.Frame(self.frame2)
        self.linha2.pack()
        self.linha3 = tk.Frame(self.frame2)
        self.linha3.pack()
        self.linha4 = tk.Frame(self.frame2)
        self.linha4.pack()
        self.linha5 = tk.Frame(self.frame2)
        self.linha5.pack()

        # Numeros
        self.b1 = tk.Button(self.linha1, text='1', font=(15))
        self.b1['padx'], self.b1['pady'] = 5, 5
        self.b1.pack(side=tk.LEFT)
        self.b2 = tk.Button(self.linha1, text='2')
        self.b2.pack(side=tk.LEFT)
        self.b3 = tk.Button(self.linha1, text='3')
        self.b3.pack(side=tk.LEFT)

        self.b4 = tk.Button(self.linha2, text='4')
        self.b4.pack(side=tk.LEFT)
        self.b5 = tk.Button(self.linha2, text='5')
        self.b5.pack(side=tk.LEFT)
        self.b6 = tk.Button(self.linha2, text='6')
        self.b6.pack(side=tk.LEFT)

        self.b7 = tk.Button(self.linha3, text='7')
        self.b7.pack(side=tk.LEFT)
        self.b8 = tk.Button(self.linha3, text='8')
        self.b8.pack(side=tk.LEFT)
        self.b9 = tk.Button(self.linha3, text='9')
        self.b9.pack(side=tk.LEFT)

        self.b0 = tk.Button(self.linha4, text='0')
        self.b0.pack(side=tk.BOTTOM)


raiz = tk.Tk()
raiz.geometry("250x300")
Calculadora(raiz)
raiz.mainloop()
