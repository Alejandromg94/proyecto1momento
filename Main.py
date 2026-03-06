estudiantes = {}

def registrar_ingreso():
    nombre = input("Ingrese el nombre del estudiante: ")
    
    if nombre in estudiantes:
        print("El estudiante ya está registrado.")
    else:
        estudiantes[nombre] = []
        print("Estudiante registrado correctamente.")