# Definir variables
Inversion_1, Inversion_2, Inversion_3, Total = 0.0, 0.0, 0.0, 0.0

print("Inversión de una empresa")
print("===================================")

# Solicitar al usuario las cantidades invertidas de las tres personas
Inversion_1 = float(input("Cantidad invertida de la primer persona: "))
Inversion_2 = float(input("Cantidad invertida de la segunda persona: "))
Inversion_3 = float(input("Cantidad invertida de la tercer persona: "))

Total = Inversion_1 + Inversion_2 + Inversion_3

# Calcular y mostrar el porcentaje invertido de cada persona
print("El porcentaje invertido de la primer persona es:", (Inversion_1 / Total) * 100, "%")
print("El porcentaje invertido de la segunda persona es:", (Inversion_2 / Total) * 100, "%")
print("El porcentaje invertido de la tercer persona es:", (Inversion_3 / Total) * 100, "%")
