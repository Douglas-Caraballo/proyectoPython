from baseDeDatos import consultasBBDD
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def verificacionRuta():
    ruta = './reportes'

    try:
        os.makedirs(ruta)

        return ruta

    except FileExistsError:

        return ruta


def reporte():

    today = datetime.today()

    fillName = "Prueba Pdf {}-{}-{}.pdf".format(today.day, today.month, today.year)
    filledir = verificacionRuta()

    outfillepath = os.path.join(filledir, fillName)

    lienzo = canvas.Canvas(outfillepath)

    lienzo.setLineWidth(0.3)
    lienzo.drawString(30, 750, "Prueba para generar pdf al momento de dar click para futuros reportes")
    lienzo.line(20,740,140,740)
    lienzo.showPage()
    lienzo.save()



