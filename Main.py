estudiantes = {}

def registrar_ingreso():
    nombre = input("Ingrese el nombre del estudiante: ")
    
    if nombre in estudiantes:
        print("El estudiante ya está registrado.")
    else:
        estudiantes[nombre] = []
        print("Estudiante registrado correctamente.")
        
def registrar_nota():
    nombre = input("Ingrese el nombre del estudiante: ")
    
    if nombre not in estudiantes:
        print("El estudiante no está registrado.")
        return
    
    try:
        nota = float(input("Ingrese la nota (0 a 5): "))
        
        if 0 <= nota <= 5:
            estudiantes[nombre].append(nota)
            print("Nota registrada correctamente.")
        else:
            print("La nota debe estar entre 0 y 5.")
    
    except ValueError:
        print(" Debe ingresar un número válido.")