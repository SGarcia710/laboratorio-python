import pandas as pd
import subprocess, platform
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

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
    bd = pd.read_csv('bd.csv')
    print(bd.to_string(index = False))
    pause = input("\nPresione cualquier tecla para continuar")

  def generarPDF(self):
    self.limpiarConsola()
    cedulaBusqueda = int(input("Por favor digite la cedula del usuario al cual desea generar reporte => "))
    bd = pd.read_csv('bd.csv')
    i = 0
    index = 0
    while i<len(bd):
      if bd['CC'][i] == int(cedulaBusqueda):
        index = i
      i += 1
    nombreArchivo = "Informe"+bd['Nombre'][index]+".pdf"
    c = canvas.Canvas(nombreArchivo, pagesize=letter)
    medidaX, medidaY = letter#medidas (612.0, 792.0)


    c.setFont("Helvetica", 16)
    c.drawString(medidaX/2-125, 720, "Laboratorio Clinico Sanitas S.A.")
    c.setFont("Helvetica", 12)
    c.drawString(65,650, "Nombre:")
    nomStr = str(bd['Nombre'][index])
    c.drawString(120,650, nomStr)
    c.drawString(360,650, "Documento:")
    cedStr = str(bd['CC'][index])
    c.drawString(435,650, cedStr)
    c.drawString(65,630, "Fecha de Ingreso:")
    fecStr = str(bd['Fecha de Ingreso'][index])
    c.drawString(170,630, fecStr)
    c.drawString(300,630, "Edad:")
    edadStr = str(bd['Edad'][index])    
    c.drawString(335,630, edadStr)
    c.drawString(390,630, "Sexo:")
    sexStr = str(bd['Sexo'][index])
    c.drawString(425,630, sexStr)
    c.drawString(65,600,"Examen")
    c.drawString(300,600,"Resultados")
    c.drawString(380,600,"Valores de Referencia")
    primerFila = 580
    if bd['Glicemia'][index] == "si":
      resultado = input("Ingrese el resultado del examen de Glicemia => ")
      valores = "0.5 - 11"
      c.drawString(65,primerFila,"Glicemia")
      c.drawString(300,primerFila, str(resultado))
      c.drawString(380,primerFila, str(valores))
      primerFila = primerFila-20
    if bd['Acido Urico'][index] == "si":
      resultado = input("Ingrese el resultado del examen de Acido Urico => ")
      valores = "100 - 200"
      c.drawString(65,primerFila,"Acido Urico")
      c.drawString(300,primerFila, str(resultado))
      c.drawString(380,primerFila, str(valores))
      primerFila = primerFila-20

    if bd['Parcial de Orina'][index] == "si":
      resultado = input("Ingrese el resultado del examen de Parcial de Orina => ")
      valores = "5 - 24"
      c.drawString(65,primerFila,"Parcial de Orina")
      c.drawString(300,primerFila, str(resultado))
      c.drawString(380,primerFila, str(valores))
      primerFila = primerFila-20

    if bd['Perfil Lipidico'][index] == "si":
      resultado = input("Ingrese el resultado del examen de Perfil Lipidico => ")
      valores = "50 - 100"
      c.drawString(65,primerFila,"Perfil Lipidico")
      c.drawString(300,primerFila, str(resultado))
      c.drawString(380,primerFila, str(valores))
      primerFila = primerFila-20

    c.save()
    pause = input("\nPresione cualquier tecla para continuar")

  def limpiarConsola(self):
    if platform.system()=="Windows":
      subprocess.Popen("cls", shell=True).communicate() 
    else: 
      print("\033c", end="")

#ejecucion del programa
Programa()
