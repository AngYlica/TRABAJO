# Definir variables
Precio, Ganancia, Venta = 0.0, 0.0, 0.0

print("Saber precio del artículo con ganancia del 30%")
print("==============================")

# Solicitar al usuario el precio del artículo
Precio = float(input("Escribe el precio del artículo: "))

# Calcular la ganancia y el precio de venta
Ganancia = Precio * 0.30
Venta = Precio + Ganancia

# Mostrar el precio al que se deben vender los artículos para obtener el 30% de ganancia
print(f"Debe vender los artículos a: ${Venta}")
print("Para obtener el 30% de ganancia")
