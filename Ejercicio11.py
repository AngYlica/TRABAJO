# Definir variables
Salario, Incremento, Nuevo_salario = 0.0, 0.0, 0.0

print("Incremento de salario del 25%")
print("==============================")

# Solicitar al usuario su salario actual
Salario = float(input("Escribe Tu Salario actual: "))

# Calcular el incremento y el nuevo salario
Incremento = Salario * 0.25
Nuevo_salario = Salario + Incremento

# Mostrar el nuevo salario con el incremento del 25%
print("Tu nuevo salario con el incremento del 25% es:", Nuevo_salario)
