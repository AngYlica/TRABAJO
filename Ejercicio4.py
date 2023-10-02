# Definir variables
examen = 0.0
nota = 0.0
parcial1 = 0.0
parcial2 = 0.0
parcial3 = 0.0
trabajo = 0.0

print("Dime la nota del parcial 1:")
parcial1 = float(input())
print("Dime la nota del parcial 2:")
parcial2 = float(input())
print("Dime la nota del parcial 3:")
parcial3 = float(input())
print("Dime la nota del examen:")
examen = float(input())
print("Dime la nota del trabajo:")
trabajo = float(input())

nota = ((parcial1 + parcial2 + parcial3) / 3) * 0.55 + 0.3 * examen + 0.15 * trabajo

print("Nota final:", nota)
