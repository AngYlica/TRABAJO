from datetime import datetime

# Solicitar la fecha de nacimiento al usuario
fecha_nacimiento_str = input("Ingresa tu fecha de nacimiento (formato: aaaa-mm-dd):")

# Convertir la fecha de nacimiento a un objeto datetime
fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d")

# Obtener la fecha actual
fecha_actual = datetime.now()

# Calcular la diferencia en años
edad = fecha_actual.year - fecha_nacimiento.year

# Comprobar si ya ha pasado el cumpleaños de este año
if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
    edad -= 1

# Mostrar la edad
print("Tu edad es: " + str(edad) + " años.")
