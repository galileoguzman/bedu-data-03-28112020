IVA = 0.16

precios_sin_iva = [415, 90, 355, 385, 115, 100, 250, 660]

for precio in precios_sin_iva:
    resultado = precio * (1 + IVA) # 104.48726378623
    resultado = round(resultado, 2) # 104.4
    resultado_impreso = f'${precio} con IVA incluido: ${resultado}'
    print(resultado_impreso)
