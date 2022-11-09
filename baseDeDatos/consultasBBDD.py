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
                CATEGORIA_ID INTEGER,
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

        myCursor.execute("INSERT INTO CATEGORIAS (NOMBRE_CATEGORIA) VALUES(%s)",(valor,))

        myBBDD.commit()
        myCursor.close()
        myBBDD.close()

        messagebox.showinfo("Base de Datos", "Se ha agregado la categoria "+valor+" de forma exitosa")

        nombreCategoria.delete(0,END)
    except:
        messagebox.showerror("Base de Datos", "Ocurrio un error al momento de guardar la categoria")

def limpiarCategoria(nombreCategoria):
    nombreCategoria.delete(0,END)

def listaCategorias(frameListaCategorias):
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
        listaLablel.grid(row=2, column=1, padx=10, pady=10)

        for i in myResult:
            listaLablel.insert(i[0], i[1])
    except:
        messagebox.showerror("","Error al momento de mostrar las categorias")