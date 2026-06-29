# archivos.py
# Responsabilidad: Leer y escribir datos en el archivo JSON.

import json

ARCHIVO: str = "alumnos.json"

def cargar_datos() -> list:
    """Carga la lista de alumnos desde el archivo JSON."""
    try:
        with open(ARCHIVO, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(lista_alumnos: list) -> None:
    """Guarda la lista de alumnos en el archivo JSON."""
    with open(ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump(lista_alumnos, archivo, indent=4, ensure_ascii=False)

