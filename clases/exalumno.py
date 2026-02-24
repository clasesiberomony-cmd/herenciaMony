#Referencias
from clases.alumno import Alumno
from clases.profesor import Profesor

class Exalumno(Alumno,Profesor):
  def __init__(self):
    super().__init__()
    self.titulo = ""
  
  def leerDatosExalumno(self):
    self.titulo = input("Título del exalumno: ")

  def mostrarDatosExalumno(self):
    print(self.titulo)