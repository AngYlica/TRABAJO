# Definir variables
Edad = 0
Pulsaciones = 0.0

print("Pulsaciones por segundo de acuerdo a tu edad")
print("==============================")

# Solicitar al usuario su edad
Edad = int(input("Escribe tu edad: "))

# Calcular las pulsaciones
Pulsaciones = (220 - Edad) / 10

# Mostrar el número de pulsaciones de acuerdo a la edad
print("El número de pulsaciones de acuerdo a tu edad es:", Pulsaciones)
