def mostrar_menu():
    """
    Muestra el menú de opciones en pantalla.
    """
    print("\n" + "=" * 42)
    print("        GESTION DE ALUMNOS")
    print("=" * 42)
    print("  1. Registrar alumno")
    print("  2. Listar alumnos")
    print("  3. Buscar alumno")
    print("  4. Modificar alumno")
    print("  5. Eliminar alumno")
    print("  6. Ver estadisticas")
    print("  7. Salir")
    print("=" * 42)

def pedir_dni():
    """
    Solicita un DNI al usuario.

    Returns:
        str: DNI ingresado por el usuario.
    """
    return input("  Ingrese DNI: ")

def pedir_datos():
    """
    Solicita los datos de un alumno al usuario.

    Returns:
        tuple: (dni, nombre, apellido, edad, nota)
    """
    dni = input("  DNI: ")
    nombre = input("  Nombre: ")
    apellido = input("  Apellido: ")
    edad = input("  Edad: ")
    nota = input("  Nota: ")
    return dni, nombre, apellido, edad, nota

def mostrar_alumno(alumno):
    """
    Muestra los datos de un alumno en formato legible.

    Args:
        alumno (dict): Diccionario con los datos del alumno.
                       Si es None, muestra "Alumno no encontrado."
    """
    if alumno is None:
        print("Alumno no encontrado.")
        return
    print(f"  DNI: {alumno['dni']}")
    print(f"  Nombre: {alumno['nombre']}")
    print(f"  Apellido: {alumno['apellido']}")
    print(f"  Edad: {alumno['edad']}")
    print(f"  Nota: {alumno['nota']}")