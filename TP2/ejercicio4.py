def vender_zapallos(nombre_comprador, tipo_divisa):
    """
    Vende zapallos, aplicando descuentos según el tipo de divisa.

    Args:
        nombre_comprador: Nombre del comprador.
        tipo_divisa: Tipo de divisa utilizada para el pago (dólar, yen, guaraní, peso u otra).
    """

    precio_base = 1000  # Precio base del zapallo en pesos
    descuentos = {"dólar": 0.05, "yen": 0.15, "guaraní": 0.20, "peso": 0.10}
    
    # Verificar si la divisa tiene descuento
    descuento = descuentos.get(tipo_divisa.lower(), 0.1)  # 10% de incremento por defecto

    # Calcular el descuento y el precio final
    precio_con_descuento = precio_base * (1 - descuento)

    # Convertir el precio final a pesos si la divisa es diferente al peso argentino
    tipo_cambio = {
        "dólar": 200,  # Ajustar según el tipo de cambio actual
        "yen": 0.005,  # Ajustar según el tipo de cambio actual
        "guaraní": 0.0005  # Ajustar según el tipo de cambio actual
    }
    precio_en_pesos = precio_con_descuento * tipo_cambio.get(tipo_divisa.lower(), 1)

    # Emitir el recibo
    print("-" * 30)
    print("Recibo de Venta")
    print("-" * 30)
    print(f"Nombre del comprador: {nombre_comprador}")
    print(f"Producto: Zapallo")
    print(f"Cantidad: 1")
    print(f"Tipo de divisa: {tipo_divisa}")
    print(f"Descuento: {descuento * 100:.2f}%")
    print(f"Precio total (en pesos): ${precio_en_pesos:.2f}")
    print("-" * 30)

# Solicitar datos al usuario
nombre = input("Ingrese el nombre del comprador: ")
divisa = input("Ingrese el tipo de divisa (dólar, yen, guaraní, peso u otra): ")

# Llamar a la función para vender el zapallo
vender_zapallos(nombre, divisa)