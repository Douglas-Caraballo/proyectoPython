import mysql.connector
from tkinter import messagebox

def crearBBDD():
    try:
        myBBDD = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )

        myCursor= myBBDD.cursor()

        myCursor.execute('''
            CREATE DATABASE PYTHONSYSTEM;

            USE PRUEBAS;

            CREATE TABLE CATEGORIAS(
                ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                NOMBRE_CATEGORIA VARCHAR(30)
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
