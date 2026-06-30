from archivos import cargar_datos, guardar_datos
from validaciones import validar_dni, validar_edad, validar_nota, validar_nombre, validar_apellido


def registrar_alumno(dni, nombre, apellido, edad, nota):
    """
    Registra un nuevo alumno si los datos son válidos.

    Args:
        dni (str): DNI del alumno.
        nombre (str): Nombre del alumno.
        apellido (str): Apellido del alumno.
        edad (str): Edad del alumno.
        nota (str): Nota del alumno.

    Returns:
        tuple: (True, "Alumno registrado con exito.") si se registró.
               (False, mensaje_error) si hubo un error.
    """
    lista = cargar_datos()
    
    #validar DNI
    valido, resultado = validar_dni(dni, lista)
    if not valido:
        return False, resultado
    dni = resultado
    
    #validar nombre
    valido, resultado = validar_nombre(nombre)
    if not valido:
        return False, resultado
    nombre = resultado
    
    #validar apellido
    valido, resultado = validar_apellido(apellido)
    if not valido:
        return False, resultado
    apellido = resultado
    
    #validar edad
    valido, resultado = validar_edad(edad)
    if not valido:
        return False, resultado
    edad = resultado
    
    #validar nota
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
    """
    Devuelve la lista completa de alumnos.

    Returns:
        list: Lista de diccionarios con todos los alumnos.
    """
    return cargar_datos()


def buscar_alumno(dni):
    """
    Busca un alumno por DNI.

    Args:
        dni (str): DNI del alumno a buscar.

    Returns:
        dict: Diccionario con los datos del alumno si existe.
        None: Si no se encuentra.
    """
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
    """
    Modifica los datos de un alumno existente.

    Args:
        dni (str): DNI del alumno a modificar.
        nuevo_nombre (str): Nuevo nombre.
        nuevo_apellido (str): Nuevo apellido.
        nueva_edad (str): Nueva edad.
        nueva_nota (str): Nueva nota.

    Returns:
        tuple: (True, "Alumno modificado con exito.") si se modificó.
               (False, mensaje_error) si hubo un error.
    """
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
    
    # Validar nombre
    valido, resultado = validar_nombre(nuevo_nombre)
    if not valido:
        return False, resultado
    nuevo_nombre = resultado
    
    # Validar apellido
    valido, resultado = validar_apellido(nuevo_apellido)
    if not valido:
        return False, resultado
    nuevo_apellido = resultado
    
    # Validar edad
    valido, resultado = validar_edad(nueva_edad)
    if not valido:
        return False, resultado
    edad = resultado
    
    # Validar nota
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
    """
    Elimina un alumno por su DNI.

    Args:
        dni (str): DNI del alumno a eliminar.

    Returns:
        tuple: (True, "Alumno eliminado con exito.") si se eliminó.
               (False, mensaje_error) si hubo un error.
    """
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