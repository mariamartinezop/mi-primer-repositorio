import calendar

def es_fecha_valida(dia, mes, anio):

    if anio < 0 or mes < 1 or mes > 12 or dia < 1:
        return False

    return dia <= calendar.monthrange(anio, mes)[1]

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

if es_fecha_valida(dia, mes, anio):
    print("La fecha es válida.")
else:
    print("La fecha no es válida.")