import pandas as pd
import subprocess, platform
# from fpdf import FPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

 

# print("HOLA")

# bd = pandas.read_csv('bd.csv')
# print(bd)

# my_dict = { 'nom' : ["Jaime Rodriguez Villada", "Marcela Garcia Rodriguez", "Ruben Dario Pardo Ramos", "Fredy Ortiz Ortiz"],
#                    'fech' : ["23/03/19","24/03/19", "26/03/19", "26/03/19"],
#                    'cc': [123456, 908765, 324578, 105925],
#                    'edad': [28,22,24,25],
#                    'sex': ['M','F','M','M']
#                    }

# my_dict['nom'].append("Sebastian Garcia")
# my_dict['fech'].append("10/05/19")
# my_dict['cc'].append(123812)
# my_dict['edad'].append(23)
# my_dict['sex'].append('M')

# f= open("bd.csv","w+")crear archivo
# f=open("bd.csv", "a+")
# f.write("Sebastian Garcia,10/05/19,123456,23,M\n")
# print(f)
# f.close() 

# df = pd.DataFrame(my_dict,index = ['Nombre', 'Fecha de Ingreso', 'C.C.', 'Edad', 'Sexo'])
# df = pd.DataFrame(my_dict)
# df.columns = ['Nombre', 'Fecha de Ingreso', 'C.C.', 'Edad', 'Sexo']
# print(df.to_string(index = False))

class Programa:  
  def __init__(self):
    self.bd = pd.read_csv('bd.csv')
    self.menu()

  def menu(self):
    op = 9
    while op!=0:
      self.limpiarConsola()
      print ("Menu Laboratorio Clinico")
      print ("[1] Ingresar Usuario")
      print ("[2] Ver Usuarios")
      print ("[3] Generar Informe Usuario")
      print ("[0] Salir")
      op = int(input("\t\tOpcion => "))
      # op = 3
      if(op == 1):
        self.ingresarUsuario()
      elif(op == 2):
        self.verUsuarios()
      elif(op == 3):
        self.generarPDF()

  def ingresarUsuario(self):
    self.limpiarConsola()
    print ("\t\t\tINGRESO DE USUARIOS:")
    nombre = input("Digite los Nombres y Apellidos del paciente => ")
    fecha = input("Digite la Fecha de Ingreso del paciente (dd/mm/aaaa) => ")
    cedula = input("Digite el numero de Cedula del paciente => ")
    edad = input("Digite la Edad del paciente => ")
    sexo = input("Digite Sexo del paciente (M: Masculino F: Femenino) => ")
    print("\t\t\tLISTA DE EXAMENES:")
    print("\tGlicemia")
    gli = input("\t\t=> ")  
    print("\tAcido Urico")
    uri = input("\t\t=> ")    
    print("\tParcial de Orina")
    ori = input("\t\t=> ")    
    print("\tPerfil Lipidico")
    lipi = input("\t\t=> ")
    string = nombre+","+fecha+","+cedula+","+edad+","+sexo+","+gli+","+uri+","+ori+","+lipi+"\n"
    f=open("bd.csv", "a+")
    f.write(string)
    f.close() 

    pause = input("\nPresione cualquier tecla para continuar")
  
  def verUsuarios(self):
    self.limpiarConsola()
    print ("\t\t\t\t\t\tLISTA DE USUARIOS:")
    print(self.bd.to_string(index = False))
    pause = input("\nPresione cualquier tecla para continuar")
  # def buscarEnDataFrame(self, dato):
  #   i = 0
  #   print(len(self.bd['CC']['0'].index))
  #   # while i<self.db.shape[]
  def generarPDF(self):
    self.limpiarConsola()
    cedulaBusqueda = input("Por favor digite la cedula del usuario al cual desea generar reporte => ")
    # for e in self.bd['CC']:
      # if
    # print(self.bd['CC'])
    print(len(self.bd))
    i = 0
    index = 0
    while i<len(self.bd):
      if self.bd['CC'][i] == cedulaBusqueda:
        index = i
      i += 1

    # print(self.bd['CC'][index],self.bd['Nombre'][index])
    # print(self.buscarEnDataFrame(int(cedulaBusqueda)))
    nombreArchivo = "Informe"+self.bd['Nombre'][index]+".pdf"
    # pdf = FPDF()
    # pdf.add_page()
    # pdf.set_font("Arial", size=12)
    # pdf.cell(200, 10, txt="Reporte Clinico", ln=1, align="C")
    # strUno = "Nombre:"
    # strDos = "Fecha de Ingreso: 25/05/2019\t\t Edad: 23\t\t Sexo: M"
    # pdf.cell(200, 10, txt="Nombre: ", ln=1, align="L")
    # pdf.cell(200, 10, txt="Cedula :", ln=1, align="L")
    # pdf.output("simple_demo.pdf")
    # print(letter)
    c = canvas.Canvas(nombreArchivo, pagesize=letter)
    medidaX, medidaY = letter
    #medidas (612.0, 792.0)
    c.setFont("Helvetica", 16)
    c.drawString(medidaX/2-125, 720, "Laboratorio Clinico Sanitas S.A.")
    c.setFont("Helvetica", 12)
    c.drawString(65,650, "Nombre:")
    nomStr = str(self.bd['Nombre'][index])
    c.drawString(120,650, nomStr)
    c.drawString(360,650, "Documento:")
    cedStr = str(self.bd['CC'][index])
    c.drawString(435,650, cedStr)
    c.drawString(65,630, "Fecha de Ingreso:")
    fecStr = str(self.bd['Fecha de Ingreso'][index])
    c.drawString(170,630, fecStr)
    c.drawString(300,630, "Edad:")
    edadStr = str(self.bd['Edad'][index])    
    c.drawString(335,630, edadStr)
    c.drawString(390,630, "Sexo:")
    sexStr = str(self.bd['Sexo'][index])
    c.drawString(425,630, sexStr)


    c.save()
    pause = input("\nPresione cualquier tecla para continuar")

  def limpiarConsola(self):
    if platform.system()=="Windows":
      subprocess.Popen("cls", shell=True).communicate() #I like to use this instead of subprocess.call since for multi-word commands you can just type it out, granted this is just cls and subprocess.call should work fine 
    else: #Linux and Mac
      print("\033c", end="")

#ejecucion del programa
Programa()