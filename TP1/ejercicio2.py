nota1=float(input("ingrese la nota del primer parcial: "))
nota2=float(input("ingresa la nota del segundo parcial: "))
promedio= (nota1+nota2)/2
print(promedio)
#nota de ultimo examen
if nota2 >= 7:
    print("Aprobo el ultimo examen")
else: 
    print("Desaprobo el ultimo examen")
#evolucion del desempeño
if nota2 > nota1:
    print("Mejoro su desempeño")
elif nota2 == nota1:
    print ("Mantuvo la nota")
else:
    print("Empeoro su desempeño")
if promedio >= 7:
    print("Promociono")
elif promedio >= 4 and promedio < 7:
    print("Debe rendir final")
else: 
    print("Debe recursar")
