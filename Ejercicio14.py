# Definir variables
a, b, c, Promedio = 0.0, 0.0, 0.0, 0.0

print("Cronometración del tiempo de la semana de ejercicios")
print("=========================================")
print("Escribe los tiempos de la semana")
print("Día 1")
a = float(input())
print("Día 2")
b = float(input())
print("Día 3")
c = float(input())

# Calcular el promedio de los tiempos
Promedio = (a + b + c) / 3

# Mostrar el promedio de tiempo recorrido en la semana
print("El Promedio de tiempo recorrido en la semana es:", Promedio)
