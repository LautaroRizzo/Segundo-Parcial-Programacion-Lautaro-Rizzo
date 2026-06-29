from alumnos import(
    registrar_alumno,
    listar_alumnos,
    buscar_alumno,
    modificar_alumno,
    eliminar_alumno,

)

from estadistica import calcular_estadisticas
from menu import mostrar_menu, pedir_datos, pedir_dni, mostrar_alumno

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
    
        if opcion == "1":
            print("REGISTRAR ALUMNO")
            dni, nombre, apellido, edad, nota = pedir_datos()
            exito, mensaje = registrar_alumno(dni, nombre, apellido, edad, nota)
            print(mensaje)
        
        elif opcion == "2":
            print("LISTA DE ALUMNOS")
            alumnos = listar_alumnos()
            if not alumnos:
                print("No hay alumnos registrados.")
            else:
                for alumno in alumnos:
                    print("-" * 35)
                    mostrar_alumno(alumno)
                print("-" * 35)
        
        elif opcion == "3":
            print("BUSCAR ALUMNO")
            dni = pedir_dni()
            alumno = buscar_alumno(dni)
            if alumno:
                mostrar_alumno(alumno)
            else:
                print("Alumno no encontrado.")
        elif opcion == "4":
            print("MODIFICAR ALUMNO")
            dni = pedir_dni()
            alumno = buscar_alumno(dni)
            
            if alumno is None:
                print("Alumno no encontrado.")
            else:
                print("  (Deje en blanco para mantener el valor actual)")
                nuevo_nombre = input(f"  Nombre ({alumno['nombre']}): ") or alumno['nombre']
                nuevo_apellido = input(f"  Apellido ({alumno['apellido']}): ") or alumno['apellido']
                nueva_edad = input(f"  Edad ({alumno['edad']}): ") or str(alumno['edad'])
                nueva_nota = input(f"  Nota ({alumno['nota']}): ") or str(alumno['nota'])
                exito, mensaje = modificar_alumno(dni, nuevo_nombre, nuevo_apellido, nueva_edad, nueva_nota)
                print(mensaje)
        
        elif opcion == "5":
            print("ELIMINAR ALUMNO")
            dni = pedir_dni()
            mensaje = eliminar_alumno(dni)
            print(mensaje)
        
        elif opcion == "6":
            print("ESTADISTICAS")
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