from tkinter import *
from tkinter import messagebox

raiz = Tk()

#---------- Barra de menu -------------
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)

inicioMenu = Menu(barraMenu, tearoff=0)
inicioMenu.add_command(label="Salir")

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de ...")

barraMenu.add_cascade(label="Inicio", menu=inicioMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#--------- Menu lateral -------------------
frameMenu = Frame(raiz)
frameMenu.grid(row=0, column=0)

botonRegistrar = Button(frameMenu, text="Registrar")
botonRegistrar.grid(row=2, column=1, sticky="W")

botonLista = Button(frameMenu, text="Lista de Productos")
botonLista.grid(row=3,column=1, sticky="W")



raiz.mainloop()