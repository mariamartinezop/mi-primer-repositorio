def mayor_estricto(a, b, c): 
    maximo = a
    if b > maximo:
        maximo = b
    if c > maximo:
        maximo = c
    # Verificar si hay otros numeros iguales al maximo
    if a == maximo or b == maximo or c == maximo:
        if a == b or a == c or b == c:
            return None  # No hay mayor estricto
    return maximo

# Programa principal
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

resultado = mayor_estricto(num1, num2, num3)

if resultado is None:
    print("No hay un solo numero mayor entre los numeros ingresados.")
else:
    print("El mayor numero es:", resultado)