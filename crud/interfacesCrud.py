from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from baseDeDatos import consultasBBDD

def registrarProducto():
    registrarVentana = Tk()
    registrarVentana.title("Registar producto")

#------------ Frame Formulario ---------------------
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

    textCodigo = Entry(frameRegistrarVentana)
    textCodigo.grid(row=2, column=1, padx=10, pady=10)

    textPrecio = Entry(frameRegistrarVentana)
    textPrecio.grid(row=3, column=1, padx=10, pady=10)

    textCalendar = DateEntry(frameRegistrarVentana, width=18)
    textCalendar.grid(row=4, column=1, padx=10, pady=10)

    textCategoria = Combobox(frameRegistrarVentana, width=18,state="readonly")
    textCategoria.grid(row=5, column=1, padx=10, pady=10)
    listaDeCategorias = consultasBBDD.categoriasRegistroProductos()
    if(listaDeCategorias != "error"):
        textCategoria['values'] = listaDeCategorias

    textCantidad = Entry(frameRegistrarVentana)
    textCantidad.grid(row=6, column=1, padx=10, pady=10)

    #-------------- Frame Botones --------------------
    frameBotonesRegistro = Frame(registrarVentana)
    frameBotonesRegistro.pack()

    botonRegistrar = Button(frameBotonesRegistro, text= "Registrar")
    botonRegistrar.grid(row=1, column=1, padx=10, pady=10)

    botonLimiar = Button(frameBotonesRegistro, text="Limpiar Campos")
    botonLimiar.grid(row=1, column=2, padx=10, pady=10)

    registrarVentana.mainloop()

def listaDeProducto():

    ventanaListaProductos = Tk()
    ventanaListaProductos.title("Lista de productos")

    frameBuscar = Frame(ventanaListaProductos)
    frameBuscar.pack()





    ventanaListaProductos.mainloop


def salir(raiz):

    salirDelSistema = messagebox.askquestion("Salir del sistema", "Desea salir del sistema?")

    if salirDelSistema == "yes":

        raiz.destroy()

def registrarCategorias():
    categoriasVentana = Tk()
    categoriasVentana.title("Categorias")

    frameRegistroCategorias = Frame(categoriasVentana)
    frameRegistroCategorias.grid(row=0,column=1)

    nombreCategoria = StringVar()

    labelNombre = Label(frameRegistroCategorias, text="Nombre")
    labelNombre.grid(row=1,column=1, padx=10)

    cuadroNombre = Entry(frameRegistroCategorias, textvariable= nombreCategoria)
    cuadroNombre.grid(row=1, column=2, padx=10, pady=10, columnspan=2)

    botonRegistro = Button(frameRegistroCategorias, text="Registrar", command=lambda:consultasBBDD.crearCategoria(cuadroNombre))
    botonRegistro.grid(row=3, column=1, padx=10, pady=10)

    botonLimpiar= Button(frameRegistroCategorias, text="Limpiar Campos", command=lambda:consultasBBDD.limpiarCategoria(cuadroNombre))
    botonLimpiar.grid(row=3, column=3, padx=10, pady=10)

    frameListaCategorias = Frame(categoriasVentana)
    frameListaCategorias.grid(row=1,column=1)

    labelCategorias = Label(frameListaCategorias, text="Categorias:")
    labelCategorias.grid(row=1,column=1,pady=10,sticky="nesw")

    consultasBBDD.listaCategorias(frameListaCategorias,categoriasVentana)