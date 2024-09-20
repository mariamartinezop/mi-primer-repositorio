num_dias = 6
aula_par = "A-300"
aula_impar = "A-315"

print("============= Listado de aulas =============")
print("Día\tAula")
for dia in range(1, num_dias + 1):
    aula = aula_par if dia % 2 == 0 else aula_impar

    print(dia, "\t", aula)