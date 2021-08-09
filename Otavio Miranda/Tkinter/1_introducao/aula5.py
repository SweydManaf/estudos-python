from tkinter import *

raiz = Tk()
raiz.title("Primeira app")

# Redimensionamento da janela
raiz.geometry("500x250+200+200")
raiz.resizable(True, True)

# Definir o icone
raiz.iconbitmap("images/yt_download.ico")


# raiz.minsize(width=500, height=250)
# raiz.maxsize(700, 400)

# raiz.state("zoomed") # janela maximizada
# raiz.state("iconic") # janela minimizada



raiz.mainloop()
