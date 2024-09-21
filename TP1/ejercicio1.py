# Datos personales
nombre = input("Ingrese el nombre del alumno: ")
edad = int(input("Ingrese la edad del alumno: "))
fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (DD/MM/AAAA): ")
tiene_titulo_secundario = True

# Matrícula y cuota
monto_matricula = float(input("Ingrese el monto de la matrícula: "))
cuota = monto_matricula + 1000

# Python 
arancel_python_i = 12000
cursa_python_i = input("¿Cursará Python I? (Sí/No): ")
if cursa_python_i.lower() == "sí":
    cuota += arancel_python_i

# Costo mensual y descuento
costo_mensual = cuota / 4  # Asumimos 4 meses por cuatrimestre

# Descuento por pago en efectivo
pago_efectivo = input("¿Pagará en efectivo? (Sí/No): ")
if pago_efectivo.lower() == "sí":
    descuento = costo_mensual * 0.15
    costo_mensual -= descuento

print("===========================================================")
print("========== Universidad de python - Inscripciones ==========")
print("===========================================================")
print("\nResumen de Inscripción:")
print("Nombre:", nombre)
print("Edad:", edad)
print("Fecha de Nacimiento:", fecha_nacimiento)
print("Posee Título Secundario:", tiene_titulo_secundario)
print("Monto de Matrícula:", monto_matricula)
print("Cuota Total:", cuota)
print("Costo Mensual:", costo_mensual)