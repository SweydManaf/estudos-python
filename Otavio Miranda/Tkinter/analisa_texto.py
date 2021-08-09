from tkinter import *
from tkinter import ttk

master = Tk()


def on_write(*args):
    num = var.get()

    if len(num) > 0:
        if not num[-1].isdigit():
            var.set(num[:-1])
        else:
            var.set(num[:max_len])


max_len = 5
var = StringVar()
var.trace('w', on_write)

entrada = Entry(master, textvariable=var)
entrada.pack()

master.mainloop()