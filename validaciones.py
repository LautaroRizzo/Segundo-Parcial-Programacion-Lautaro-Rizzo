def validar_dni(dni: str, lista_alumnos: list, dni_original: int = None):
    """Verifica que el DNI sea válido y no esté duplicado."""
    try:
        dni: int = int(dni)
    except ValueError:
        return False, "El DNI debe ser un número entero."
    
    if dni <= 0:
        return False, "El DNI no puede ser negativo o cero."
    
    for alumno in lista_alumnos:
        if alumno["dni"] == dni and dni != dni_original:
            return False, f"El DNI {dni} ya está registrado."
    
    return True, dni


def validar_edad(edad: str):
    """Verifica que la edad sea un número entero no negativo."""
    try:
        edad_int: int = int(edad)
    except ValueError:
        return False, "La edad debe ser un número entero."
    
    if edad_int < 0:
        return False, "La edad no puede ser negativa."
    
    return True, edad_int

def validar_nota(nota: str):
    """Verifica que la nota sea un número entre 0 y 10."""
    try:
        nota_float: float = float(nota)
    except ValueError:
        return False, "La nota debe ser un número."
    
    if 0 <= nota_float <= 10:
        return True, nota_float
    else:
        return False, "La nota debe estar entre 0 y 10."