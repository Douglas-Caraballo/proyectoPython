from tkinter import *
from tkinter import messagebox

def RegistrarProducto():
    registrarVentana = Tk()
    registrarVentana.title("Registar producto")

    frameRegistrarVentana = Frame(registrarVentana)
    frameRegistrarVentana.pack()



    labelNombre = Label(frameRegistrarVentana, text="Nombre")
    labelNombre.grid(row=1, column=0, sticky="W", padx=10, pady=10)

    labelCodigo = Label(frameRegistrarVentana, text= "Codigo")
    labelCodigo.grid(row=2, column=0, sticky="W" ,padx=10, pady=10)

    labelPrecio = Label(frameRegistrarVentana, text="Precio")
    labelPrecio.grid(row=3, column=0, sticky="W", padx=10, pady=10)

    labelFecha = Label(frameRegistrarVentana, text="Fecha")
    labelFecha.grid(row=4, column=0, sticky="W", padx=10, pady=10)

    labelCategoria = Label(frameRegistrarVentana, text="Categoria")
    labelCategoria.grid(row=5, column=0, sticky="W", padx=10, pady=10)

    labelCantidad = Label(frameRegistrarVentana, text="Cantidad")
    labelCantidad.grid(row=6, column=0, sticky="W", padx=10, pady=10)

    textNombre = Entry(frameRegistrarVentana)
    textNombre.grid(row=1,column=1, padx=10, pady=10)


    registrarVentana.mainloop()