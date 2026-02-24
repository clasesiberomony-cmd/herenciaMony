#referencia
from clases.exalumno import Exalumno

def main():
    exa = Exalumno()
    exa.leerDatosPersona()
    exa.leerDatosAlumno()
    exa.leerDatosProfesor()
    exa.leerDatosExalumno()
    print("********************")
    exa.mostrarDatosPersona()
    exa.mostrarDatosAlumno()
    exa.mostrarDatosProfesor()
    exa.mostrarDatosExalumno()
    
if __name__ == "__main__":
    main()