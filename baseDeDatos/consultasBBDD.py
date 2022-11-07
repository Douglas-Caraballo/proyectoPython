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

        nombreCategoria.set("")
    except:
        messagebox.showerror("Base de Datos", "Ocurrio un error al momento de guardar la categoria")
"""

    myBBDD = mysql.connector.connect(
        host=hostBBDD,
        user=userBBDD,
        password=passwordBBDD,
        database= databaseBBDD
    )
    values = (nombreCategoria.get())

    myCursor = myBBDD.cursor()

    myCursor.execute("INSERT INTO CATEGORIAS (NOMBRE_CATEGORIA) VALUES(%s)",(values,))

    myBBDD.commit()

    myCursor.close()
    myBBDD.close() """

def limpiarCategoria(nombreCategoria):
    nombreCategoria.set("")