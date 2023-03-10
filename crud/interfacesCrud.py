from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
#from tkcalendar import DateEntry
from baseDeDatos import consultasBBDD

#------ Funcion para la interface de registro de productos

def registrarProducto():
    registrarVentana = Toplevel()
    registrarVentana.config(bg="snow")
    registrarVentana.title("Registar producto")

#------------ Frame Formulario ---------------------
    frameRegistrarVentana = Frame(registrarVentana, bg="snow")
    frameRegistrarVentana.pack()

    labelNombre = Label(frameRegistrarVentana, text="Nombre", bg="snow", fg="coral2")
    labelNombre.grid(row=1, column=0, sticky="W", padx=10, pady=10)

    labelCodigo = Label(frameRegistrarVentana, text= "Codigo", bg="snow", fg="coral2")
    labelCodigo.grid(row=1, column=2, sticky="W" ,padx=10, pady=10)

    labelPrecio = Label(frameRegistrarVentana, text="Precio", bg="snow", fg="coral2")
    labelPrecio.grid(row=3, column=0, sticky="W", padx=10, pady=10)

    labelCantidad = Label(frameRegistrarVentana, text="Cantidad", bg="snow", fg="coral2")
    labelCantidad.grid(row=3, column=2, sticky="W", padx=10, pady=10)

    labelFecha = Label(frameRegistrarVentana, text="Fecha", bg="snow", fg="coral2")
    labelFecha.grid(row=4, column=0, sticky="W", padx=10, pady=10)

    labelCategoria = Label(frameRegistrarVentana, text="Categoria", bg="snow", fg="coral2")
    labelCategoria.grid(row=4, column=2, sticky="W", padx=10, pady=10)

    textNombre = Entry(frameRegistrarVentana, bg="snow2" )
    textNombre.grid(row=1,column=1, padx=10, pady=10)

    textCodigo = Entry(frameRegistrarVentana, bg="snow2")
    textCodigo.grid(row=1, column=3, padx=10, pady=10)

    textPrecio = Entry(frameRegistrarVentana, bg="snow2")
    textPrecio.grid(row=3, column=1, padx=10, pady=10)

    '''textCalendar = DateEntry(frameRegistrarVentana, width=18)
    textCalendar.grid(row=4, column=1, padx=10, pady=10)'''

    textCategoria = Combobox(frameRegistrarVentana, width=18,state="readonly")
    textCategoria.grid(row=4, column=3, padx=10, pady=10)
    listaDeCategorias = consultasBBDD.categoriasRegistroProductos()
    if(listaDeCategorias != "error"):
        textCategoria['values'] = listaDeCategorias

    textCantidad = Entry(frameRegistrarVentana)
    textCantidad.grid(row=3, column=3, padx=10, pady=10)

    #-------------- Frame Botones --------------------
    frameBotonesRegistro = Frame(registrarVentana)
    frameBotonesRegistro.config(bg="snow")
    frameBotonesRegistro.pack()

    botonRegistrar = Button(frameBotonesRegistro, text= "Registrar", command=lambda:consultasBBDD.registrarProducto(textNombre,textCodigo,textPrecio,textCategoria,textCantidad,registrarVentana))
    botonRegistrar.config(bg="cyan3", fg="salmon4", activebackground="cyan2", activeforeground="gray9")
    botonRegistrar.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    botonLiminar = Button(frameBotonesRegistro, text="Limpiar Campos", command=lambda:consultasBBDD.limpiarCamposProductos(textNombre,textCodigo,textPrecio,textCantidad))
    botonLiminar.config(bg="cyan3", fg="salmon4", activebackground="cyan2", activeforeground="gray9")
    botonLiminar.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

    registrarVentana.mainloop()

#------ Funcion para la interface de la lista de productos

def listaDeProducto():

    ventanaListaProductos = Toplevel()
    ventanaListaProductos.title("Lista de productos")
    ventanaListaProductos.config(bg="snow")

    frameBuscar = Frame(ventanaListaProductos, bg="snow")
    frameBuscar.pack()

    labelBuscarNombre = Label(frameBuscar, text="Nombre", bg="snow")
    labelBuscarNombre.grid(row=1,column=2, padx=10, pady=10)

    textNombresProducto = Entry(frameBuscar, bg="snow2")
    textNombresProducto.grid(row=1, column=3, padx=10, pady=10)

    botonBuscar = Button(frameBuscar, text="Buscar", command=lambda:consultasBBDD.buscar(textNombresProducto,productosLista))
    botonBuscar.config(bg="cyan3", activebackground="cyan2", fg="tomato4", activeforeground="gray9")
    botonBuscar.grid(row=1, column=4, padx=10, pady=10)

    frameListaProductos = Frame(ventanaListaProductos, bg="snow")
    frameListaProductos.pack()

    productosLista = Listbox(frameListaProductos, width=45, bg="peach puff")
    productosLista.grid(row=1, column=1, padx=10, pady=10, columnspan=3)
    scrolVert = Scrollbar(frameListaProductos, command= productosLista.yview)
    scrolVert.config(bg="peach puff")
    scrolVert.grid(row=1, column=4, padx=5, pady=10, sticky="nsew")

    botonLeer = Button(frameListaProductos, text= "Ver detalles", command=lambda:consultasBBDD.verProducto(productosLista))
    botonLeer.config(bg="cyan3", activebackground="cyan2", fg="tomato4", activeforeground="gray9")
    botonLeer.grid(row=2, column=1, padx=10, pady=10)

    botonEditarRegistro = Button(frameListaProductos, text="Editar", command=lambda:verParaEditar(productosLista))
    botonEditarRegistro.config(bg="cyan3", activebackground="cyan2", fg="tomato4", activeforeground="gray9")
    botonEditarRegistro.grid(row=2, column=2, padx=10, pady=10)

    botonEliminarRegistro = Button(frameListaProductos, text="Eliminar", command=lambda:consultasBBDD.eliminarProducto(ventanaListaProductos,productosLista))
    botonEliminarRegistro.config(bg="tomato2", activebackground="tomato1", fg="gray14", activeforeground="gray9")
    botonEliminarRegistro.grid(row=2, column=3, padx=10, pady=10)

    registros= consultasBBDD.leerProductos()

    if registros!= "Error":
        for i in registros:
            productosLista.insert(END, i)

    else:
        messagebox.showerror("", "Ocurrio un error al momento de mostrar los elementos")

    ventanaListaProductos.mainloop()

#------ Funcion para cerrar el sistema completo

def salir(raiz):

    salirDelSistema = messagebox.askquestion("Salir del sistema", "Desea salir del sistema?")

    if salirDelSistema == "yes":

        raiz.destroy()

#------ Funcion para la interface de registro de las categorias

def registrarCategorias():
    categoriasVentana = Toplevel(bg="snow")
    categoriasVentana.title("Categorias")


    frameRegistroCategorias = Frame(categoriasVentana, bg="snow")
    frameRegistroCategorias.grid(row=0,column=1)

    nombreCategoria = StringVar()

    labelNombre = Label(frameRegistroCategorias, text="Nombre:", bg="snow")
    labelNombre.grid(row=1,column=2, padx=20)

    cuadroNombre = Entry(frameRegistroCategorias, textvariable= nombreCategoria, bg="snow2")
    cuadroNombre.grid(row=1, column=3, pady=5, padx=20, columnspan=2)

    botonRegistro = Button(frameRegistroCategorias, text="Registrar", command=lambda:consultasBBDD.crearCategoria(cuadroNombre))
    botonRegistro.config(bg="cyan3", activebackground="cyan2", fg="tomato4", activeforeground="gray9")
    botonRegistro.grid(row=3, column=1, padx=50, pady=10, columnspan=2)

    botonLimpiar= Button(frameRegistroCategorias, text="Limpiar Campos", command=lambda:consultasBBDD.limpiarCategoria(cuadroNombre))
    botonLimpiar.config(bg="Cyan3", activebackground="cyan2", fg="tomato4", activeforeground="gray9")
    botonLimpiar.grid(row=3, column=3, padx=5, pady=10)

    frameListaCategorias = Frame(categoriasVentana, bg="snow")
    frameListaCategorias.grid(row=1,column=1)

    labelCategorias = Label(frameListaCategorias, text="Categorias Creadas", bg="snow", foreground="coral2")
    labelCategorias.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

    listaLablel = Listbox(frameListaCategorias,width=60, bg="peach puff", fg="tomato4")
    listaLablel.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

    lista= consultasBBDD.listaCategorias()

    for i in lista:
        listaLablel.insert(i[0],i[1])

    botonEditar = Button(frameListaCategorias, text="Editar Categoria",command=lambda:consultasBBDD.editarCategorias(listaLablel))
    botonEditar.config(bg="Cyan3", activebackground="Cyan2", fg="tomato4", activeforeground="gray9")
    botonEditar.grid(row=3, column=1, padx=10, pady=10)

    botonEliminar = Button(frameListaCategorias, text="Eliminar Categoria", command=lambda:consultasBBDD.eliminarCategoria(listaLablel,categoriasVentana))
    botonEliminar.config(bg="tomato3", activebackground="tomato2", fg="sienna4", activeforeground="gray9")
    botonEliminar.grid(row=3, column=2, padx=10, pady=10)

#------ Funcion para la interface que muestra la informacion de un producto para editarlo

def verParaEditar(productosLista):
    for i in productosLista.curselection():
        productoSeleccionado = productosLista.get(i)

    try:
        producto= productoSeleccionado[0]

        resultado = consultasBBDD.consultaProductos(producto)

        if resultado != "error":

            ventanaEditar = Toplevel()
            ventanaEditar.title("Editar")

            frameEditar = Frame(ventanaEditar)
            frameEditar.pack()

            labelNombre = Label(frameEditar, text="Nombre:")
            labelNombre.grid(row=0, column=0, padx=10, pady=10)

            textNombre = Entry(frameEditar, justify=CENTER)
            textNombre.insert(0, resultado[0][1])
            textNombre.grid(row=0, column=1, padx=10, pady=10)

            labelCodigo = Label(frameEditar, text="Codigo:")
            labelCodigo.grid(row=1, column=0, padx=10, pady=10)

            textCodigo = Entry(frameEditar, justify=CENTER)
            textCodigo.insert(0,resultado[0][2])
            textCodigo.grid(row=1, column=1, padx=10, pady=10)

            labelPrecio = Label(frameEditar, text="Precio:")
            labelPrecio.grid(row=2, column=0, padx=10, pady=10)

            textPrecio = Entry(frameEditar, justify=CENTER)
            textPrecio.insert(0,resultado[0][3])
            textPrecio.grid(row=2, column=1, padx=10, pady=10)

            labelFecha = Label(frameEditar, text="Fecha:")
            labelFecha.grid(row=3,column=0,padx=10, pady=10)

            textCalendar = DateEntry(frameEditar, width=18, justify=CENTER)
            textCalendar.grid(row=3, column=1, padx=10, pady=10)

            labelCategoria = Label(frameEditar, text="Categoria")
            labelCategoria.grid(row=4, column=0, padx=10, pady=10)

            textCategoria = Combobox(frameEditar,width=18,state="readonly", justify=CENTER)
            textCategoria.grid(row=4, column=1, padx=10, pady=10)
            listaDeCategorias = consultasBBDD.categoriasRegistroProductos()
            if(listaDeCategorias != "error"):
                textCategoria['values'] = listaDeCategorias

            labelCantidad = Label(frameEditar, text="Cantidad:")
            labelCantidad.grid(row=5, column=0, padx=10, pady=10)

            textCantidad = Entry(frameEditar, justify=CENTER)
            textCantidad.insert(0, resultado[0][4])
            textCantidad.grid(row=5, column=1, padx=10, pady=10)

            botonEditar=Button(frameEditar, text="Actualizar", command=lambda:consultasBBDD.editarProducto(ventanaEditar,textNombre,textCodigo,textPrecio, textCalendar,textCategoria,textCantidad,resultado[0][0]))
            botonEditar.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        else:
            messagebox.showerror("","Error al cargar los datos")

    except UnboundLocalError:
        messagebox.showerror("","Por favor seleccione un producto")