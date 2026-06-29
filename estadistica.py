from archivos import cargar_datos


def calcular_estadisticas():
    lista = cargar_datos()
    total = len(lista)
    
    if total == 0:
        return {
            "total": 0,
            "promedio": 0,
            "mayor_nota": None,
            "aprobados": 0,
            "desaprobados": 0
        }
    
    suma_notas = 0
    mayor = -1
    alumno_mayor = None
    aprobados = 0
    desaprobados = 0
    
    for alumno in lista:
        nota = alumno["nota"]
        suma_notas = suma_notas + nota
        
        if nota > mayor:
            mayor = nota
            alumno_mayor = alumno
        
        if nota >= 6:
            aprobados = aprobados + 1
        else:
            desaprobados = desaprobados + 1
    
    return {
        "total": total,
        "promedio": round(suma_notas / total, 2),
        "mayor_nota": alumno_mayor,
        "aprobados": aprobados,
        "desaprobados": desaprobados
    }