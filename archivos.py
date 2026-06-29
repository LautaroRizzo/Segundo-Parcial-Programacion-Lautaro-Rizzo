import json

ARCHIVO = "alumnos.json"

def cargar_datos():
    """
    Carga la lista de alumnos desde el archivo JSON.

    Returns:
        list: Lista de diccionarios con los datos de los alumnos.
              Si el archivo no existe, devuelve una lista vacía.
    """
    try:
        with open(ARCHIVO, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(lista_alumnos):
    """
    Guarda la lista de alumnos en el archivo JSON.

    Args:
        lista_alumnos (list): Lista de diccionarios con los datos de los alumnos.
    """
    with open(ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump(lista_alumnos, archivo, indent=4, ensure_ascii=False)