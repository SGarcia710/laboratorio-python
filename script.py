import pandas as pd
import subprocess, platform
from fpdf import FPDF
 

print("HOLA")

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
      if(op == 1):
        self.ingresarUsuario()
      elif(op == 2):
        self.verUsuarios()
      elif(op == 3):
        self.generarPDF()

  def ingresarUsuario(self):
    self.limpiarConsola()
    print ("\t\tINGRESO DE USUARIOS:")
    nombre = input("Digite los Nombres y Apellidos del paciente =>")
    fecha = input("Digite la Fecha de Ingreso del paciente (dd/mm/aaaa) =>")
    cedula = input("Digite el número de Cedula del paciente =>")
    edad = input("Digite la Edad del paciente =>")
    sexo = input("Digite Sexo del paciente (M: Masculino F: Femenino) =>")
    string = nombre+","+fecha+","+cedula+","+edad+","+sexo+"\n"
    f=open("bd.csv", "a+")
    f.write(string)
    f.close() 

    pause = input("\nPresione cualquier tecla para continuar")
  
  def verUsuarios(self):
    self.limpiarConsola()
    print ("\t\tLISTA DE USUARIOS:")
    bd = pd.read_csv('bd.csv')
    print(bd.to_string(index = False))
    pause = input("\nPresione cualquier tecla para continuar")
  
  def generarPDF(self):
    self.limpiarConsola()
    print ("aqui generas reporte PDF")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Reporte Clinico", ln=1, align="C")
    strUno = "Nombre: Sebastian Garcia\t\t C.C.: 1144195009"
    strDos = "Fecha de Ingrso: 25/05/2019\t\t Edad: 23\t\t Sexo: M"
    pdf.cell(200, 10, txt=strUno, ln=1, align="L")
    pdf.cell(200, 10, txt=strDos, ln=1, align="L")
    pdf.output("simple_demo.pdf")
    pause = input("\nPresione cualquier tecla para continuar")

  def limpiarConsola(self):
    if platform.system()=="Windows":
      subprocess.Popen("cls", shell=True).communicate() #I like to use this instead of subprocess.call since for multi-word commands you can just type it out, granted this is just cls and subprocess.call should work fine 
    else: #Linux and Mac
      print("\033c", end="")

#ejecucion del programa
Programa()