from tkinter import *

# grid manager

root = Tk()
root.title('Titulo')

label1 = Label(root, text='text', bg='red').grid(column=0)
label2 = Label(root, text='text', bg='green').grid(column=1)
label3 = Label(root, text='text', bg='green').grid(column=2)
label4 = Label(root, text='text', bg='blue').grid(columnspan=3, sticky='we')


root.mainloop()
