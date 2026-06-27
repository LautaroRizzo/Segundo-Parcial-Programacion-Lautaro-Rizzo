from archivos import cargar_datos, guardar_datos
from validaciones import validar_dni, validar_edad, validar_nota

def registrar_alumno(dni, nombre, apellido, edad, nota):
    lista = cargar_datos()
    
    valido, resultado = validar_dni(dni, lista)
    if not valido:
        return False, resultado
    dni = resultado
    
    valido, resultado = validar_edad(edad)
    if not valido:
        return False, resultado
    edad = resultado
    
    valido, resultado = validar_nota(nota)
    if not valido:
        return False, resultado
    nota = resultado
    
    alumno = {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nota": nota
    }
    
    lista = lista + [alumno]
    guardar_datos(lista)
    return True, "Alumno registrado con exito."

def listar_alumnos():
    return cargar_datos()

def buscar_alumno(dni):
    lista = cargar_datos()
    try:
        dni = int(dni)
        for alumno in lista:
            if alumno["dni"] == dni:
                return alumno
        return None
    except ValueError:
        return None

def modificar_alumno(dni, nuevo_nombre, nuevo_apellido, nueva_edad, nueva_nota):
    lista = cargar_datos()
    try:
        dni = int(dni)
    except ValueError:
        return False, "El DNI debe ser un numero."
    
    alumno_encontrado = None
    for alumno in lista:
        if alumno["dni"] == dni:
            alumno_encontrado = alumno
            break
    
    if alumno_encontrado is None:
        return False, "No se encontro un alumno con ese DNI."
    
    valido, resultado = validar_edad(nueva_edad)
    if not valido:
        return False, resultado
    edad = resultado
    
    valido, resultado = validar_nota(nueva_nota)
    if not valido:
        return False, resultado
    nota = resultado
    
    alumno_encontrado["nombre"] = nuevo_nombre
    alumno_encontrado["apellido"] = nuevo_apellido
    alumno_encontrado["edad"] = edad
    alumno_encontrado["nota"] = nota
    
    guardar_datos(lista)
    return True, "Alumno modificado con exito."

def eliminar_alumno(dni):
    lista = cargar_datos()
    try:
        dni = int(dni)
        for i, alumno in enumerate(lista):
            if alumno["dni"] == dni:
                del lista[i]
                guardar_datos(lista)
                return True, "Alumno eliminado con exito."
        return False, "No se encontro un alumno con ese DNI."
    except ValueError:
        return False, "El DNI debe ser un numero."