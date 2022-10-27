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

labelLogo = Label(frameMenu,text= "Logo")
labelLogo.grid(row=0,column=1,sticky="nsew", padx=10, pady=10)

botonRegistrar = Button(frameMenu, text="Registrar",width=15, relief="flat")
botonRegistrar.grid(row=2, column=1, sticky="W")

botonLista = Button(frameMenu, text="Lista de Productos", relief="flat")
botonLista.grid(row=3,column=1, sticky="W")

botonReportes = Button(frameMenu, text="Reportes",width=15,relief="flat")
botonReportes.grid(row=4, column=1,sticky="W")

botonSalir = Button(frameMenu, text="Salir", width=15, relief="flat")
botonSalir.grid(row=5, column=1, sticky="W")

#-------- Frame principal ------------------

framePrincipal = Frame(raiz)
framePrincipal.grid(row=0,column=1)

labelValor = Label(framePrincipal, text="El valor total del inventario: ", padx=3)
labelValor.grid(row=1, column=1)

labelRegistro = Label(framePrincipal, text="Cantidad de registros: ",padx=3)
labelRegistro.grid(row=1, column=3)

raiz.mainloop()