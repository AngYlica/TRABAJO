# Definir variables
Total = 0.0

print("Presupuesto anual de los departamentos del hospital")
print("==============================")

# Solicitar al usuario el presupuesto anual
Total = float(input("Escribe el presupuesto anual: "))

# Calcular el presupuesto para cada área
ginecologia = Total * 0.40
traumatologia = Total * 0.30
pediatria = Total * 0.30

# Mostrar el presupuesto para cada área
print("Al área de ginecología le corresponde: $", ginecologia)
print("Al área de traumatología le corresponde: $", traumatologia)
print("Al área de pediatría le corresponde: $", pediatria)
