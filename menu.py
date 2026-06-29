#funciones del menu para que el main me quede lo mas limpio posible
def mostrar_menu():
    """Muestra el menú de opciones."""
    print("GESTION DE ALUMNOS")
    print("  1. Registrar alumno")
    print("  2. Listar alumnos")
    print("  3. Buscar alumno")
    print("  4. Modificar alumno")
    print("  5. Eliminar alumno")
    print("  6. Ver estadisticas")
    print("  7. Salir")
def pedir_dni():
    """Solicita un DNI al usuario."""
    return input("  Ingrese DNI: ")

def pedir_datos():
    """Solicita los datos de un alumno al usuario."""
    dni = input("  DNI: ")
    nombre = input("  Nombre: ")
    apellido = input("  Apellido: ")
    edad = input("  Edad: ")
    nota = input("  Nota: ")
    return dni, nombre, apellido, edad, nota

def mostrar_alumno(alumno):
    """Muestra los datos de un alumno."""
    if alumno is None:
        print("Alumno no encontrado.")
        return
    print(f"  DNI: {alumno['dni']}")
    print(f"  Nombre: {alumno['nombre']}")
    print(f"  Apellido: {alumno['apellido']}")
    print(f"  Edad: {alumno['edad']}")
    print(f"  Nota: {alumno['nota']}")