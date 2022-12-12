from baseDeDatos import consultasBBDD
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime
import os
from tkinter import messagebox

def verificacionRuta():
    ruta = './reportes'

    try:
        os.makedirs(ruta)

        return ruta

    except FileExistsError:

        return ruta


def reporte():

    today = datetime.today()

    datos = consultasBBDD.consultaReportes()

    fillName = "Prueba Pdf {}-{}-{}.pdf".format(today.day, today.month, today.year)
    filledir = verificacionRuta()

    outfillepath = os.path.join(filledir, fillName)

    lienzo = canvas.Canvas(outfillepath)
    posision = 10*inch

    lienzo.setLineWidth(0.3)
    lienzo.drawString(250, 800, "Reportes de articulos")
    lienzo.line(230,790,380,790)

    if datos != "Error":
        for i in datos:
            lienzo.drawString(inch, posision, str(i))
            posision = posision-(0.5*inch)


    lienzo.showPage()
    lienzo.save()

    messagebox.showinfo("","El reporte fue generador y guardado")



