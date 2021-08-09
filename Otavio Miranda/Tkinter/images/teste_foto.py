from tkinter import *

master = Tk()
master.geometry('500x500')
def aparece(event):
    img['file'] = 'alien_1.png'
    lbl_img['image'] = img

def desaparece(event):
    img['file'] = 'espace.png'
    lbl_img['image'] = img

img = PhotoImage(file='espace.png')
lbl_img = Label(master, image=img)
lbl_img.pack()
lbl_img.bind('<Motion>', aparece)
lbl_img.bind('<Leave>', desaparece)
master.mainloop()
