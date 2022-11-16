from tkinter import messagebox
from tkinter import *
import mysql.connector

hostBBDD = "localhost"
userBBDD = "root"
passwordBBDD = ""
databaseBBDD = "PYTHONSYSTEM"

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
                CODIGO VARCHAR(30),
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
            myCursor.execute("INSERT INTO CATEGORIAS (NOMBRE_CATEGORIA) VALUES(%s)",(valor,))

            myBBDD.commit()
            myCursor.close()
            myBBDD.close()

            messagebox.showinfo("Base de Datos", "Se ha agregado la categoria '"+valor+"' de forma exitosa")

            nombreCategoria.delete(0,END)
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

    labelEditar= Label(frameEditar, text="Nomebre Categoria")
    labelEditar.grid(row=1, column=1, padx=10, pady=10)

    nombreEditar = Entry(frameEditar)
    nombreEditar.grid( row=1, column=2, padx=10, pady=10)

    editarBoton = Button(frameEditar, text="Guardar", command=lambda:editarCategoriaFuncion(ventanaEditrarCategoria,categoriaSelecionada,nombreEditar))
    editarBoton.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

def editarCategoriaFuncion(ventanaEditrarCategoria,categoriaSelecionada,nombreEditar):
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
        messagebox.showerror("Base de datos", "ocurrio un error al guardar el cambio")

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

def limpiarCamposProductos(textNombre,textCodigo,textPrecio,textCantidad):
    textNombre.delete(0,END)
    textCodigo.delete(0,END)
    textPrecio.delete(0,END)
    textCantidad.delete(0,END)