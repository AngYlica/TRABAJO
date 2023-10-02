salario_base = float(input("Indica el salario base: "))
venta1 = float(input("Indica el importe de la primera venta: "))
venta2 = float(input("Indica el importe de la segunda venta: "))
venta3 = float(input("Indica el importe de la tercera venta: "))

# Realizamos cálculos
comision = .10 * (venta1 + venta2 + venta3)
salario_total = salario_base + comision

# Mostramos en pantalla
print(f"El sueldo total a recibir es {salario_total}")
