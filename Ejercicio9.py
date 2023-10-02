# Definir variables
Masa, Presion, Volumen, Temperatura = 0.0, 0.0, 0.0, 0.0

print("SABER LA PRESIÓN, VOLUMEN Y TEMPERATURA DE UNA MASA")
print("==============================")

# Solicitar al usuario la presión, el volumen y la temperatura
Presion = float(input("Escribe la presión: "))
Volumen = float(input("Escribe el volumen: "))
Temperatura = float(input("Escribe la temperatura: "))

# Calcular la masa
Masa = (Presion * Volumen) / (0.37 * (Temperatura + 460))

# Mostrar el resultado de la masa de aire
print("El resultado de la masa de aire es:", Masa)
