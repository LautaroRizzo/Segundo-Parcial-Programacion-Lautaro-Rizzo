# main.py
# Punto de entrada del programa. Solo contiene el menú principal.

from alumnos import (
    registrar_alumno,
    listar_alumnos,
    buscar_alumno,
    modificar_alumno,
    eliminar_alumno
)
from estadistica import calcular_estadisticas
from menu import mostrar_menu, pedir_dni, pedir_datos, mostrar_alumno


def registrar_con_reintentos():
    """
    Permite registrar un alumno con reintentos en caso de error.
    
    Si el usuario ingresa datos incorrectos (DNI duplicado, edad negativa,
    nota fuera de rango), se le muestra el error y se le pregunta si
    quiere intentar de nuevo o cancelar el registro.
    
    Returns:
        None: No devuelve nada.
    """
    print("--- REGISTRAR ALUMNO ---")
    
    while True:
        dni, nombre, apellido, edad, nota = pedir_datos()
        exito, mensaje = registrar_alumno(dni, nombre, apellido, edad, nota)
        
        if exito:
            print(mensaje)
            break
        else:
            print(f"❌ {mensaje}")
            respuesta = input("¿Quiere intentar de nuevo? (s/n): ").lower()
            if respuesta != 's':
                print("Registro cancelado.")
                break


def modificar_con_reintentos():
    """
    Permite modificar un alumno con reintentos en caso de error.
    
    Primero busca el alumno por DNI. Si no existe, pregunta si quiere
    intentar de nuevo. Luego, si los nuevos datos son incorrectos
    (edad negativa o nota fuera de rango), pregunta si quiere reintentar.
    
    Returns:
        None: No devuelve nada.
    """
    print("--- MODIFICAR ALUMNO ---")
    
    while True:
        dni = pedir_dni()
        alumno = buscar_alumno(dni)
        
        if alumno is not None:
            break
        else:
            print("❌ Alumno no encontrado.")
            respuesta = input("¿Quiere intentar de nuevo? (s/n): ").lower()
            if respuesta != 's':
                print("Modificacion cancelada.")
                return
    

    while True:
        print("  (Deje en blanco para mantener el valor actual)")
        nuevo_nombre = input(f"  Nombre ({alumno['nombre']}): ") or alumno['nombre']
        nuevo_apellido = input(f"  Apellido ({alumno['apellido']}): ") or alumno['apellido']
        nueva_edad = input(f"  Edad ({alumno['edad']}): ") or str(alumno['edad'])
        nueva_nota = input(f"  Nota ({alumno['nota']}): ") or str(alumno['nota'])
        
        exito, mensaje = modificar_alumno(dni, nuevo_nombre, nuevo_apellido, nueva_edad, nueva_nota)
        
        if exito:
            print(mensaje)
            break
        else:
            print(f"❌ {mensaje}")
            respuesta = input("¿Quiere intentar de nuevo? (s/n): ").lower()
            if respuesta != 's':
                print("Modificacion cancelada.")
                break


def eliminar_con_reintentos():
    """
    Permite eliminar un alumno con reintentos en caso de error.
    
    Si el DNI ingresado no existe, pregunta si quiere intentar de nuevo
    o cancelar la eliminación.
    
    Returns:
        None: No devuelve nada.
    """
    print("--- ELIMINAR ALUMNO ---")
    
    while True:
        dni = pedir_dni()
        exito, mensaje = eliminar_alumno(dni)
        
        if exito:
            print(mensaje)
            break
        else:
            print(f"❌ {mensaje}")
            respuesta = input("¿Quiere intentar de nuevo? (s/n): ").lower()
            if respuesta != 's':
                print("Eliminacion cancelada.")
                break


def main():
    """
    Función principal del programa.
    
    Ejecuta el bucle infinito que muestra el menú y maneja las
    opciones seleccionadas por el usuario. Las opciones son:
        1. Registrar alumno (con reintentos)
        2. Listar alumnos
        3. Buscar alumno
        4. Modificar alumno (con reintentos)
        5. Eliminar alumno (con reintentos)
        6. Ver estadísticas
        7. Salir
    
    Returns:
        None: No devuelve nada.
    """
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            registrar_con_reintentos()
        
        elif opcion == "2":
            print("--- LISTAR ALUMNOS ---")
            alumnos = listar_alumnos()
            if not alumnos:
                print("  No hay alumnos registrados.")
            else:
                for alumno in alumnos:
                    print("-" * 35)
                    mostrar_alumno(alumno)
                print("-" * 35)
        
        elif opcion == "3":
            print("--- BUSCAR ALUMNOS ---")
            dni = pedir_dni()
            alumno = buscar_alumno(dni)
            if alumno:
                mostrar_alumno(alumno)
            else:
                print("Alumno no encontrado.")
        
        elif opcion == "4":
            modificar_con_reintentos()
        
        elif opcion == "5":
            eliminar_con_reintentos()
        
        elif opcion == "6":
            print("--- ESTADISTICAS ---")
            stats = calcular_estadisticas()
            print(f"  Total de alumnos: {stats['total']}")
            if stats['total'] > 0:
                print(f"  Promedio de notas: {stats['promedio']}")
                mayor = stats['mayor_nota']
                print(f"  Mayor nota: {mayor['nombre']} {mayor['apellido']} (DNI: {mayor['dni']}) - Nota: {mayor['nota']}")
                print(f"  Aprobados (>= 6): {stats['aprobados']}")
                print(f"  Desaprobados (< 6): {stats['desaprobados']}")
        
        elif opcion == "7":
            print("¡Hasta luego! Saliendo del sistema...")
            break
        
        else:
            print("Opcion no valida. Elija 1-7.")
main()