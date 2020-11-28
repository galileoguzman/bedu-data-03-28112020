IVA = 0.16

precios_con_iva = [415, 90, 355, 385, 115, 100, 250, 660]

for precio in precios_con_iva:
    resultado = precio * (1 + IVA)
    print(f'${precio} con IVA incluido: $', round(resultado, 2))
