from cProfile import label
from tkinter import *
import random
import tkinter as tk

root = Tk()
root.geometry("300x100")
root.title("CARA O CRUZ JUEGO")
root.resizable(width=False, height=False)

def Ventana2():
    root = Tk()
    root.geometry("300x100")
    root.title("Acerca de")
    root.resizable(width=False, height=False)
    label3 = Label(root,text="EZEQUIEL MARTIN 2023")
    label3.place(x=40,y=40)

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar)
filemenu.add_command(label="Salir",command=quit)
filemenu.add_command(label="Acerca de",command=Ventana2)

menubar.add_cascade(label="Opciones", menu=filemenu)


root.config(menu=menubar)

var = StringVar()

nombre = StringVar()

def Ramdom():
    comienza = random.randint(0, 1)
    if comienza == 0:
        var.set('Cara',)
    else:
        var.set('Cruz')
        numero = random.randint(1,6)

Entry1 = Entry(root,textvariable=var,state="disabled")
Entry1.place(x=50,y=50)

Label1 = Label(root,text="¿Cara o Cruz?",state="disabled",font="red")
Label1.place(x=75,y=10)

boton1 = Button(root,text="Random",command=Ramdom)
boton1.place(x=200,y=48)

root.mainloop()



