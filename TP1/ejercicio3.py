dia= int(input("ingrese el numero de dia: 1 (lunes) a 6 (sabado): "))
if dia% 2==0:
    aula= "A-300"
else:
    aula= "A-315"
print("el aula asignada para el dia", dia, "es:", aula)
#descuento cuota
valor_cuota= float(input("ingrese el valor de la cuota: "))
turno= input("ingrese el turno (mañana/tarde/noche: ")
num_materias = int(input("ingrese el numero de materias: "))
if turno== "tarde" and num_materias > 3:
    descuento= valor_cuota*0.25
else:
    descuento = valor_cuota*0.05
cuota_final = valor_cuota - descuento
print(cuota_final)
#costo_de estacionamiento
medio_transporte = input("ingrese el medio de transporte (auto, moto, bicicleta: )")
if medio_transporte == "auto":
    costo_estacionamiento = 300
elif medio_transporte == "moto":
    costo_estacionamiento = 300
elif medio_transporte == "bicicleta":
    costo_estacionamiento = 50
print("el costo de estacionamiento es: ", costo_estacionamiento)