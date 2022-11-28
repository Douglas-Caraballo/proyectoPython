from tkinter import messagebox
from tkinter import *
import mysql.connector

hostBBDD = "localhost"
userBBDD = "root"
passwordBBDD = ""
databaseBBDD = "PYTHONSYSTEM"
tableUne = "PRODUCTOS"
tableTwo = "CATEGORIAS"

def crearBBDD():
    try:
        myBBDD = mysql.connector.connect(
            host=hostBBDD,
            user=userBBDD,
            password=passwordBBDD,
        )

        myCursor= myBBDD.cursor()

        myCursor.execute('''
            CREATE DATABASE PYTHONSYSTEM;

            USE PYTHONSYSTEM;

            CREATE TABLE CATEGORIAS(
                ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                NOMBRE_CATEGORIA VARCHAR(30) NOT NULL
            );

            CREATE TABLE PRODUCTOS(
                ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                NOMBRE_PRODUCTO VARCHAR(30),
                CODIGO VARCHAR(30) UNIQUE,
                PRECIO INTEGER,
                FECHA DATE,
                CATEGORIA_ID INTEGER NOT NULL,
                CANTIDAD INTEGER NOT NULL,
                CONSTRAINT CATEGORIAS_NOMBRES FOREIGN KEY(CATEGORIA_ID) REFERENCES CATEGORIAS(ID)
                ON DELETE CASCADE ON UPDATE CASCADE
            )''')

        messagebox.showinfo("Base de datos", "Se ha creado la base de datos")

    except:
        messagebox.showerror("Base de datos", "La base de datos ya existe")


def crearCategoria(nombreCategoria):
    try:
        myBBDD = mysql.connector.connect(
            host=hostBBDD,
            user=userBBDD,
            password=passwordBBDD,
            database= databaseBBDD
        )
        myCursor = myBBDD.cursor()
        valor = nombreCategoria.get()

        if len(valor):
            if valor[0] != " ":
                myCursor.execute("INSERT INTO CATEGORIAS (NOMBRE_CATEGORIA) VALUES(%s)",(valor,))

                myBBDD.commit()
                myCursor.close()
                myBBDD.close()

                messagebox.showinfo("Base de Datos", "Se ha agregado la categoria '"+valor+"' de forma exitosa")

                nombreCategoria.delete(0,END)
            else:
                messagebox.showerror("","No puedes guardar un elemento con espacio en blanco antes del contenido")
        else:
            messagebox.showerror("", "Los campos no deben estar vacios")
    except:
        messagebox.showerror("Base de Datos", "Ocurrio un error al momento de guardar la categoria")

def limpiarCategoria(nombreCategoria):
    nombreCategoria.delete(0,END)

def listaCategorias(frameListaCategorias,categoriasVentana):
    try:
        myBBDD = mysql.connector.connect(
            host = hostBBDD,
            user = userBBDD,
            password = passwordBBDD,
            database = databaseBBDD
        )

        myCursor = myBBDD.cursor()
        myCursor.execute("SELECT * FROM CATEGORIAS")

        myResult = myCursor.fetchall()

        listaLablel = Listbox(frameListaCategorias,width=40)
        listaLablel.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        for i in myResult:
            listaLablel.insert(i[0],i[1])

        botonEditar = Button(frameListaCategorias, text="Editar Categoria",command=lambda:editarCategorias(listaLablel))
        botonEditar.grid(row=3, column=1, padx=10, pady=10)

        botonEliminar = Button(frameListaCategorias, text="Eliminar Categoria", command=lambda:eliminarCategoria(listaLablel,categoriasVentana))
        botonEliminar.grid(row=3, column=2, padx=10, pady=10)
    except:
        messagebox.showerror("","Error al momento de mostrar las categorias")

def editarCategorias(listaLablel):

    for i in listaLablel.curselection():
        categoriaSelecionada=listaLablel.get(i)

    ventanaEditrarCategoria = Tk()
    ventanaEditrarCategoria.title("Editar Categoria")

    frameEditar = Frame(ventanaEditrarCategoria)
    frameEditar.pack()

    labelEditar= Label(frameEditar, text="Nombre Categoria")
    labelEditar.grid(row=1, column=1, padx=10, pady=10)

    nombreEditar = Entry(frameEditar)
    nombreEditar.grid( row=1, column=2, padx=10, pady=10)

    editarBoton = Button(frameEditar, text="Guardar", command=lambda:editarCategoriaFuncion(ventanaEditrarCategoria,categoriaSelecionada,nombreEditar))
    editarBoton.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

def editarCategoriaFuncion(ventanaEditrarCategoria,categoriaSelecionada,nombreEditar):
    if len(nombreEditar.get()):
        if nombreEditar.get()[0] != ' ':
            try:
                myBBDD = mysql.connector.connect(
                    host=hostBBDD,
                    user=userBBDD,
                    password=passwordBBDD,
                    database= databaseBBDD
                )
                myCursor = myBBDD.cursor()
                valor = nombreEditar.get()

                myCursor.execute("UPDATE CATEGORIAS SET NOMBRE_CATEGORIA = %s WHERE NOMBRE_CATEGORIA='"+ categoriaSelecionada+"'", (valor,))
                myBBDD.commit()
                myCursor.close()
                myBBDD.close()

                messagebox.showinfo("Base de datos", "La categoria fue editada con éxito")

                ventanaEditrarCategoria.destroy()

            except:
                messagebox.showerror("Base de datos", "Ocurrio un error al guardar el cambio")
        else:
            messagebox.showerror("","No puede haber espacios en blanco antes del contenido")
    else:
        messagebox.showerror("", "El campo nombre no debe estar en blanco")

def eliminarCategoria(listaLablel,categoriasVentana):
    for i in listaLablel.curselection():
        categoriaSelecionada=listaLablel.get(i)

    eliminar=messagebox.askquestion("Base de datos", "¿Desea Eliminar la categoria "+ categoriaSelecionada + "? No se podrá recuperar")
    if eliminar=="yes":
        try:
            myBBDD = mysql.connector.connect(
                host=hostBBDD,
                user=userBBDD,
                password=passwordBBDD,
                database= databaseBBDD
            )
            myCursor = myBBDD.cursor()

            myCursor.execute("DELETE FROM CATEGORIAS WHERE NOMBRE_CATEGORIA='"+ categoriaSelecionada+"'")
            myBBDD.commit()
            myCursor.close()
            myBBDD.close()

            messagebox.showinfo("Base de Datos", "La categoria: '" + categoriaSelecionada +"' Fue elminada")
            categoriasVentana.destroy()

        except:
            messagebox.showerror("Base de datos", "No se pudo eliminar la categoria '" + categoriaSelecionada +"'")

def categoriasRegistroProductos():
    try:
        myBBDD = mysql.connector.connect(
                host=hostBBDD,
                user=userBBDD,
                password=passwordBBDD,
                database= databaseBBDD
            )
        myCursor = myBBDD.cursor()

        myCursor.execute("SELECT * FROM CATEGORIAS")

        myResult = myCursor.fetchall()

        myCursor.close()
        myBBDD.close()
        return myResult

    except:
        return "error"

def registrarProducto(textNombre,textCodigo,textPrecio,textCalendar,textCategoria,textCantidad,registrarVentana):
    categoria = [int(categoria) for categoria in str.split(textCategoria.get()) if categoria.isdigit()]
    for c in categoria:
        idCategoria = c
    if len(textNombre.get()) and len(textCodigo.get()):
        if textNombre.get()[0] != ' ' and textCodigo.get()[0] != ' ':
            try:
                myBBDD = mysql.connector.connect(
                        host=hostBBDD,
                        user=userBBDD,
                        password=passwordBBDD,
                        database= databaseBBDD
                    )
                myCursor = myBBDD.cursor()
                valor = [textNombre.get(), textCodigo.get(), float(textPrecio.get()), str(textCalendar.get_date()), idCategoria, int(textCantidad.get())]

                myCursor.execute("INSERT INTO PRODUCTOS (NOMBRE_PRODUCTO, CODIGO, PRECIO, FECHA, CATEGORIA_ID, CANTIDAD) VALUES (%s, %s, %s, %s, %s, %s)", (valor))
                myBBDD.commit()
                myCursor.close()
                myBBDD.close()

                continuarRegistros=messagebox.askquestion("", "El producto '"+textNombre.get()+"' se ha registrado. ¿Desea registrar otro?")
                if continuarRegistros == "yes":
                    limpiarCamposProductos(textNombre,textCodigo,textPrecio,textCantidad)
                else:
                    registrarVentana.destroy()
            except ValueError:
                messagebox.showerror("","Los valores para la cantidad y precio deben ser numericos")
            except:
                messagebox.showerror("","Se produjo un error al momento de registrar")
        else:
            messagebox.showerror("", "No se puede registrar la el elemento con un espacio en blanco al comienzo")
    else:
        messagebox.showerror("","No se pueden hacer registro en blanco")

def limpiarCamposProductos(textNombre,textCodigo,textPrecio,textCantidad):
    textNombre.delete(0,END)
    textCodigo.delete(0,END)
    textPrecio.delete(0,END)
    textCantidad.delete(0,END)

def leerProductos():
    try:
        myBBDD = mysql.connector.connect(
            host=hostBBDD,
            user=userBBDD,
            password=passwordBBDD,
            database= databaseBBDD
        )
        myCursor = myBBDD.cursor()
        myCursor.execute("SELECT ID, NOMBRE_PRODUCTO FROM "+tableUne)
        myResult = myCursor.fetchall()

        return myResult
    except:

        return "Error"

def verProducto(productosLista):
    for i in productosLista.curselection():
        productoSeleccionado = productosLista.get(i)

    try:
        producto = productoSeleccionado[0]
        myBBDD = mysql.connector.connect(
                            host=hostBBDD,
                            user=userBBDD,
                            password=passwordBBDD,
                            database= databaseBBDD
                        )

        myCursor = myBBDD.cursor()

        myCursor.execute("SELECT A.ID, A.NOMBRE_PRODUCTO, A.CODIGO, A.PRECIO, A.FECHA, B.NOMBRE_CATEGORIA, A.CANTIDAD FROM "+tableUne+" AS A JOIN "+tableTwo+" AS B ON A.CATEGORIA_ID = B.ID WHERE A.ID ="+str(producto))

        myResult = myCursor.fetchall()

        ventanaVer = Tk()
        ventanaVer.title("Producto")

        frameVer = Frame(ventanaVer)
        frameVer.pack()

        labelID = Label(frameVer, text="ID")
        labelID.grid(row=1, column=1,padx=10, pady=10)

        labelNombre = Label(frameVer, text="Nombre")
        labelNombre.grid(row=2, column=1, padx=10, pady=10)

        lablelCodigo = Label(frameVer, text="Codigo")
        lablelCodigo.grid(row=3, column=1, padx=10, pady=10)

        labelPrecio = Label(frameVer, text="Precio")
        labelPrecio.grid(row=4, column=1, padx=10, pady=10)

        labelFecha = Label(frameVer, text="Fecha de registro")
        labelFecha.grid(row=5, column=1, padx=10, pady=10)

        labelCategoria = Label(frameVer, text="Categoria")
        labelCategoria.grid(row=6, column=1, padx=10, pady=10)

        labelCantidad = Label(frameVer, text="Cantidad")
        labelCantidad.grid(row=7, column=1, padx=10, pady=10)

        textID = Entry(frameVer,justify=CENTER)
        textID.insert(0,myResult[0][0])
        textID.grid(row=1, column=2, padx=10, pady=10)

        textNombre = Entry(frameVer,justify=CENTER)
        textNombre.insert(0,myResult[0][1])
        textNombre.grid(row=2, column=2, padx=10, pady=10)

        textCodigo = Entry(frameVer, justify=CENTER)
        textCodigo.insert(0, myResult[0][2])
        textCodigo.grid(row=3, column=2, padx=10, pady=10)

        textPrecio = Entry(frameVer, justify=CENTER)
        textPrecio.insert(0,myResult[0][3])
        textPrecio.grid(row=4, column=2, padx=10, pady=10)

        textFecha = Entry(frameVer, justify=CENTER)
        textFecha.insert(0, myResult[0][4])
        textFecha.grid(row=5, column=2, padx=10, pady=10)

        textCategoria = Entry(frameVer, justify=CENTER)
        textCategoria.insert(0, myResult[0][5])
        textCategoria.grid(row=6, column=2, padx=10, pady=10)

        textCantidad = Entry(frameVer, justify=CENTER)
        textCantidad.insert(0, myResult[0][6])
        textCantidad.grid(row=7, column=2, padx=10, pady=10)

        myCursor.close()
        myBBDD.close()

    except UnboundLocalError:
        messagebox.showerror("", "Por favor seleccionar un producto")
    except:
        messagebox.showerror("","Ocurrio un error al momento de mostrar los datos")

def consultaProductos(producto):

    try:
        myBBDD = mysql.connector.connect(
                                host=hostBBDD,
                                user=userBBDD,
                                password=passwordBBDD,
                                database= databaseBBDD
                            )

        myCursor = myBBDD.cursor()

        myCursor.execute("SELECT ID, NOMBRE_PRODUCTO, CODIGO, PRECIO, CANTIDAD FROM "+tableUne+" WHERE ID="+str(producto))

        myResult = myCursor.fetchall()

        myCursor.close()
        myBBDD.close()

        return myResult

    except:

        return "error"

def editarProducto(ventanaEditar,textNombre,textCodigo,textPrecio, textCalendar,textCategoria,textCantidad, ID):

    categoria = [int(categoria) for categoria in str.split(textCategoria.get()) if categoria.isdigit()]
    for c in categoria:
        idCategoria = c

    try:
        valor = [textNombre.get(), textCodigo.get(), float(textPrecio.get()), str(textCalendar.get_date()), idCategoria, int(textCantidad.get())]
        myBBDD = mysql.connector.connect(
                                    host=hostBBDD,
                                    user=userBBDD,
                                    password=passwordBBDD,
                                    database= databaseBBDD
                                )

        myCursor = myBBDD.cursor()

        myCursor.execute("UPDATE "+tableUne+" SET NOMBRE_PRODUCTO = %s, CODIGO = %s , PRECIO = %s, FECHA = %s, CATEGORIA_ID= %s, CANTIDAD=%s WHERE ID="+str(ID),(valor))

        myBBDD.commit()

        messagebox.showinfo("","El registro se actualizo de manera correcta")

        ventanaEditar.destroy()

    except ValueError:
        messagebox.showerror("","Los valores para la cantidad y precio deben ser numericos")

    except UnboundLocalError:
        messagebox.showerror("", "Por favor seleccionar una categoria")

    except:
        messagebox.showerror("","Se produjo un error al momento de actualizar el registro")

def eliminarProducto(ventanaListaProductos,productosLista):
    for i in productosLista.curselection():
        productoSeleccionado = productosLista.get(i)

    try:
        producto = productoSeleccionado[0]
        nombre = productoSeleccionado[1]

        myBBDD = mysql.connector.connect(
                                        host=hostBBDD,
                                        user=userBBDD,
                                        password=passwordBBDD,
                                        database= databaseBBDD
                                    )

        myCursor = myBBDD.cursor()

        eliminar = messagebox.askquestion("", "Desea eliminar el registro '"+nombre+"'? No se podrá recuperar")

        if eliminar == "yes":

            myCursor.execute("DELETE FROM "+tableUne+ " WHERE ID= "+str(producto))
            myBBDD.commit()

            myCursor.close()
            myBBDD.close()

            messagebox.showinfo("",nombre+" Fue eliminado con éxito")

            ventanaListaProductos.destroy()

    except UnboundLocalError:
        messagebox.showerror("", "Por favor seleccione un producto para eliminar")

    except:
        messagebox.showerror("", "Ocurrio un problema al momento de eliminar")