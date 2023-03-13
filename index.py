from tkinter import *
from PIL import Image, ImageTk
from baseDeDatos import consultasBBDD
from crud import interfacesCrud
from crud import generarReportes

raiz = Tk()
raiz.title("Inventario")
raiz.config(bg="snow")


#---------- Barra de menu -------------


barraMenu = Menu(raiz, bg="snow", activebackground="coral1", activeforeground="white")
raiz.config(menu=barraMenu)

inicioMenu = Menu(barraMenu, tearoff=0)
inicioMenu.add_command(label="Crear base de datos", command=lambda:consultasBBDD.crearBBDD())
inicioMenu.add_separator()
inicioMenu.add_command(label="Salir", command=lambda:interfacesCrud.salir(raiz))

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de ...")

barraMenu.add_cascade(label="Inicio", menu=inicioMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


#--------- Menu lateral -------------------
frameMenu = Frame(raiz, bg="coral2")
frameMenu.grid(row=0, column=0, sticky="ns")

'''image = Image.open("img/DK-logo.png")
img = image.resize((100,100))
miLogo = ImageTk.PhotoImage(img)'''

labelLogo = Label(frameMenu,text="miLogo", bg="coral2")
labelLogo.grid(row=0,column=1, sticky="nsew", padx=15, pady=15)

botonRegistrar = Button(frameMenu, text="Registrar", height=2, fg="gray9", activeforeground="white", bg="coral2", activebackground="coral1", relief="flat", borderwidth=0, highlightthickness=0, cursor="cross", command=lambda:interfacesCrud.registrarProducto())
botonRegistrar.grid(row=2, column=1, sticky="ew")

botonCategorias = Button(frameMenu, text="Categorias", height=2, fg="gray9", activeforeground="white", bg="coral2",  activebackground="coral1", relief="flat", borderwidth=0, highlightthickness=0, cursor="cross", command=lambda:interfacesCrud.registrarCategorias())
botonCategorias.grid(row=3, column=1, sticky="ew")

botonLista = Button(frameMenu, text="Lista de Productos", height=2, activeforeground="white", fg="gray9", bg="coral2",  activebackground="coral1", relief="flat", borderwidth=0, highlightthickness=0, cursor="cross", command=lambda:interfacesCrud.listaDeProducto())
botonLista.grid(row=4,column=1, sticky="ew")

botonReportes = Button(frameMenu, text="Reportes", height=2, relief="flat", activeforeground="white", fg="gray9", bg="coral2",  activebackground="coral1", borderwidth=0, highlightthickness=0, cursor="cross", command=lambda:generarReportes.reporte())
botonReportes.grid(row=5, column=1,sticky="ew")

botonSalir = Button(frameMenu, text="Salir", height=2, relief="flat", activeforeground="white", fg="gray9", bg="coral2",  activebackground="coral1", borderwidth=0, highlightthickness=0, command=lambda:interfacesCrud.salir(raiz))
botonSalir.grid(row=6, column=1, sticky="ew")

#-------- Frame principal ------------------

framePrincipal = Frame(raiz, height=5, bg="bisque")
framePrincipal.grid(row=0, column=1)

frameValor = Frame(framePrincipal, bg="spring green")
frameValor.grid(row=0, column=0, padx=15, pady=15)

labelValor = Label(frameValor, text="El valor total del inventario: ", bg="spring green", width=40, height=10, activeforeground="OrangeRed4", border=5)
labelValor.grid(row=0, column=0, sticky="n")

frameRegistros = Frame(framePrincipal, bg="cyan3")
frameRegistros.grid(row=2, column=1, padx=15, pady=15)

labelRegistro = Label(frameRegistros, text="Cantidad de registros: ", bg="Cyan3", width=40, height=10, padx=3, activeforeground="OrangeRed4")
labelRegistro.grid(row=2, column=1)


raiz.mainloop()