import tkinter as tk
from tkinter import ttk
raiz = tk.Tk()
raiz['bg'] = 'red'
raiz.geometry("500x500")

for r in range(10):
    for c in range(5):
        frame = tk.Frame(raiz)
        frame.grid(row=r, column=c)

        button = tk.Button(frame, text=f'Linha {r} Coluna {c}')
        button['bg'] = 'darkgray'
        button["padx"], button['pady'] = 35, 3
        button.pack()

raiz.mainloop()
