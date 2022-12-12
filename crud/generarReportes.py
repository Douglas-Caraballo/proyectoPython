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
    posisionY = 10*inch

    lienzo.setLineWidth(0.3)
    lienzo.drawString(250, 800, "Reportes de articulos")
    lienzo.line(230,790,380,790)
    lienzo.drawString(inch, 10.5*inch, "Producuto")
    lienzo.drawString(2.4*inch,10.5*inch, "Codigo")
    lienzo.drawString(3.4*inch,10.5*inch, "Precio" )
    lienzo.drawString(4.5*inch,10.5*inch, "Fecha")
    lienzo.drawString(5.4*inch,10.5*inch, "Categoria")
    lienzo.drawString(6.5*inch,10.5*inch, "Cantidad")

    if datos != "Error":
        for i in datos:
            lienzo.drawString(inch, posisionY, str(i[0]))
            lienzo.drawString(2.55*inch, posisionY, str(i[1]))
            lienzo.drawString(3.45*inch, posisionY, str(i[2]))
            lienzo.drawString(4.4*inch, posisionY, str(i[3]))
            lienzo.drawString(5.45*inch, posisionY, str(i[4]))
            lienzo.drawString(6.9*inch, posisionY, str(i[5]))
            posisionY = posisionY-(0.4*inch)


    lienzo.showPage()
    lienzo.save()

    messagebox.showinfo("","El reporte fue generador y guardado")



