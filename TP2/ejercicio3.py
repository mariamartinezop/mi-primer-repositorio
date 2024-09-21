def calcular_vuelto(total_compra, dinero_recibido):

    if dinero_recibido < total_compra:
        return "Dinero insuficiente"

    vuelto = dinero_recibido - total_compra
    billetes = [500, 100, 50, 20, 10, 5, 1]
    cantidad_billetes = {}

    for billete in billetes:
        cantidad = vuelto // billete
        cantidad_billetes[billete] = cantidad
        vuelto -= cantidad * billete

    return cantidad_billetes

# Solicitar datos al usuario
total_compra = float(input("Ingrese el total de la compra: $"))
dinero_recibido = float(input("Ingrese el dinero recibido: $"))

# Calcular el vuelto
resultado = calcular_vuelto(total_compra, dinero_recibido)

# Mostrar el resultado
if isinstance(resultado, str):
    print(resultado)
else:
    print("Vuelto a entregar:")
    for billete, cantidad in resultado.items():
        if cantidad > 0:
            print(f"{cantidad} billete(s) de ${billete}")