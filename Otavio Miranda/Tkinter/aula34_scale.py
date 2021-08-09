from tkinter import *
from tkinter import ttk

master = Tk()
master.geometry('300x200')

slide = Scale(master,
              from_=0, to=100,
              orient=HORIZONTAL,
              resolution=10)
slide.pack()


def verificar():
    print(slide.get())

btn = Button(master,
             text='ver valor',
             command=verificar).pack()


master.mainloop()