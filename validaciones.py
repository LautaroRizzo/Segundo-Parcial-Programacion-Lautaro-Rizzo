def validar_dni(dni, lista_alumnos, dni_original=None):
    """
    Verifica que el DNI sea válido y no esté duplicado.

    Args:
        dni (str): DNI a validar.
        lista_alumnos (list): Lista de alumnos existentes.
        dni_original (int, optional): DNI original cuando se modifica un alumno.
                                      Default es None.

    Returns:
        tuple: (True, dni_int) si es válido.
               (False, mensaje_error) si no es válido.
    """
    try:
        dni = int(dni)
    except ValueError:
        return False, "El DNI debe ser un número entero."
    
    if dni <= 0:
        return False, "El DNI no puede ser negativo o cero."
    
    for alumno in lista_alumnos:
        if alumno["dni"] == dni and dni != dni_original:
            return False, f"El DNI {dni} ya está registrado."
    
    return True, dni

def validar_edad(edad):
    """
    Verifica que la edad sea un número entero no negativo.

    Args:
        edad (str): Edad a validar.

    Returns:
        tuple: (True, edad_int) si es válida.
               (False, mensaje_error) si no es válida.
    """
    try:
        edad = int(edad)
    except ValueError:
        return False, "La edad debe ser un número entero."
    
    if edad < 0:
        return False, "La edad no puede ser negativa."
    
    return True, edad

def validar_nota(nota):
    """
    Verifica que la nota sea un número entre 0 y 10.

    Args:
        nota (str): Nota a validar.

    Returns:
        tuple: (True, nota_float) si es válida.
               (False, mensaje_error) si no es válida.
    """
    try:
        nota = float(nota)
    except ValueError:
        return False, "La nota debe ser un número."
    
    if 0 <= nota <= 10:
        return True, nota
    else:
        return False, "La nota debe estar entre 0 y 10."