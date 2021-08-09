from tkinter import *

master = Tk()
master.title("Titulo")
master.geometry('500x500')


label2 = Label(master)
label2['text'] = 'Texto da label 2'
label2['font'] = 'Arial 20'
label2['bd'] = 1
label2['relief'] = 'solid'
label2.pack()

for k in label2.keys():
    print(f'{k} -> {label2[k]}')

master.mainloop()
