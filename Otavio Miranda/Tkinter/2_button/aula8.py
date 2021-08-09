from tkinter import *

raiz = Tk()
raiz.title("Titulo")

# Dimensoes da janela
largura = 800
altura = 400

# Resolucao da tela do sistema
largura_screen = raiz.winfo_screenwidth()
altura_screen = raiz.winfo_screenheight()

# Posicao da janela
posx = int(largura_screen/2 - largura/2)
posy = int(altura_screen/2 - altura/2)

# Define o redimensionamento da janela
raiz.geometry(f"{largura}x{altura}+{posx}+{posy}")


raiz.mainloop()