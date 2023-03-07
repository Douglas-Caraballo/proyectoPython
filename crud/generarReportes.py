from baseDeDatos import consultasBBDD
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime
import os
from tkinter import messagebox

#------- Veifica si existe la ruta y si no existe la crea------

def verificacionRuta():
    ruta = './reportes'

    try:
        os.makedirs(ruta)

        return ruta

    except FileExistsError:

        return ruta


#------ Funciones para crear el header y el footer de PDF

class PDF(FPDF):
    def header(self):
        margin=10

        celda=210-(2*margin)
        #logo
        logo="./img/DK-logo.png"
        if os.path.exists(logo):
            self.image(logo,10,8,40,40)
        #tipo de letra
        self.set_font('Arial','B',15)
        #mover a la derecha
        self.cell(80)
        #titulo
        self.cell(30,10,"Reportes de articulos",0,0,'C')
        #salto de linea
        self.ln(40)

        self.set_font('Arial','B',12)

        self.cell((celda/5),10,"Producuto",0,0,"C")
        self.cell((celda/5),10,"Codigo",0,0,"C")
        self.cell((celda/7),10,"Precio",0,0,"C")
        self.cell((celda/6),10,"Fecha",0,0,"C")
        self.cell((celda/5),10,"Categoria",0,0,"C")
        self.cell((celda/8),10,"Cantidad",0,1,"C")

        self.ln(5)

    def footer(self):
        #Posicion a 1.5 cm
        self.set_y(-15)
        #Tipo de letra
        self.set_font('Arial','I',8)
        #Paginacion
        self.cell(0,10,'Page '+str(self.page_no())+'/{nb}',0,0,'C')

#------- Funcion para generar el PDF

def reporte():

    margin=10

    celda=210-(2*margin)

    today = datetime.today()

    consulta = consultasBBDD.consultaReportes()
    totales = consultasBBDD.totales()

    fillname = "Reporte Inventario {}-{}-{}.pdf".format(today.day, today.month, today.year)
    filldir = verificacionRuta()

    outfillepath = os.path.join(filldir, fillname)

    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times','',12)

    if consulta != "Error":
        for i in consulta:
            pdf.cell((celda/4.5),10,str(i[0]),0,0)
            pdf.cell((celda/5),10,str(i[1]),0,0,'C')
            pdf.cell((celda/7.5),10,str(i[2]),0,0,'C')
            pdf.cell((celda/6),10,str(i[3]),0,0,'C')
            pdf.cell((celda/5),10,str(i[4]),0,0)
            pdf.cell((celda/9),10,str(i[5]),0,1,'C')

        pdf.ln(10)

        pdf.cell((celda/3),10, "Cantidad: "+str(totales[0][0][0]),0,0,"C")
        pdf.cell((celda/3),10, "Registros: "+str(totales[1][0][0]),0,0,"C")
        pdf.cell((celda/3),10, "Valor Total: "+str(totales[2][0][0])+"$",0,0,"C")

        pdf.output(outfillepath)

        messagebox.showinfo("","El reporte fue generador y guardado")

    else:
        messagebox.showerror("", "Ocurrió un error al momento de generar el reporte")

