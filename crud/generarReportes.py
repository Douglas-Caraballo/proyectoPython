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

def header(lienzo):

    logo = "./img/DK-logo.png"

    if os.path.exists(logo):
            lienzo.drawImage(logo,inch,10.3*inch, 100,100,mask="auto")

    lienzo.setLineWidth(0.3)
    lienzo.drawString(250, 10.8*inch, "Reportes de articulos")
    lienzo.line(230,10.7*inch,380,10.7*inch)
    lienzo.drawString(inch, 9.8*inch, "Producuto")
    lienzo.drawString(2.4*inch,9.8*inch, "Codigo")
    lienzo.drawString(3.4*inch,9.8*inch, "Precio" )
    lienzo.drawString(4.5*inch,9.8*inch, "Fecha")
    lienzo.drawString(5.4*inch,9.8*inch, "Categoria")
    lienzo.drawString(6.5*inch,9.8*inch, "Cantidad")



def reporte():

    today = datetime.today()

    datos = consultasBBDD.consultaReportes()

    fillName = "Reporte Inventario {}-{}-{}.pdf".format(today.day, today.month, today.year)
    filledir = verificacionRuta()

    outfillepath = os.path.join(filledir, fillName)

    lienzo = canvas.Canvas(outfillepath)
    posisionY = 9.3*inch

    header(lienzo)

    if datos != "Error":
        for i in datos:
            lienzo.drawString(inch, posisionY, str(i[0]))
            lienzo.drawString(2.55*inch, posisionY, str(i[1]))
            lienzo.drawString(3.45*inch, posisionY, str(i[2]))
            lienzo.drawString(4.4*inch, posisionY, str(i[3]))
            lienzo.drawString(5.45*inch, posisionY, str(i[4]))
            lienzo.drawString(6.9*inch, posisionY, str(i[5]))
            posisionY = posisionY-(0.4*inch)


    total = consultasBBDD.totales()

    lienzo.drawString(inch, inch, "Cantidad: "+str(total[0][0][0]))
    lienzo.drawString(3.5*inch, inch, "Registros: "+str(total[1][0][0]))
    lienzo.drawString(5.5*inch, inch, "Valor total: "+str(total[2][0][0])+"$")
    lienzo.showPage()
    lienzo.save()

    messagebox.showinfo("","El reporte fue generador y guardado")



