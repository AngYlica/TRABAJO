# Solicitar el número de hombres y mujeres
hombres = int(input("Ingrese el número de hombres: "))
mujeres = int(input("Ingrese el número de mujeres: "))

# Calcular el total de estudiantes
totalEstudiantes = hombres + mujeres

# Calcular el porcentaje de hombres y mujeres
porcentajeHombres = (hombres / totalEstudiantes) * 100.0
porcentajeMujeres = (mujeres / totalEstudiantes) * 100.0

# Mostrar los resultados
print(f"Porcentaje de hombres: {porcentajeHombres}%")
print(f"Porcentaje de mujeres: {porcentajeMujeres}%")

