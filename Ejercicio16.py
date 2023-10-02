# Definir variables
Exam, a, b, c, Pro_1, Pro_2, Pro_3, Pro_General = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

print("Promedio de las materias")
print("=========================")

# Materia - Matemáticas
print("Matemáticas")
Exam = float(input("Escribe la calificación del examen: "))
a = float(input("Escribe la calificación del primer trabajo: "))
b = float(input("Escribe la calificación del segundo trabajo: "))
c = float(input("Escribe la calificación del tercer trabajo: "))

Tarea = (a + b + c) / 3
Pro_1 = (Exam * 0.90) + (Tarea * 0.10)

# Materia - Física
print("=========================")
print("Física")
Exam = float(input("Escribe la calificación del examen: "))
a = float(input("Escribe la calificación del primer trabajo: "))
b = float(input("Escribe la calificación del segundo trabajo: "))

Tarea = (a + b) / 2
Pro_2 = (Exam * 0.80) + (Tarea * 0.20)

# Materia - Química
print("=========================")
print("Química")
Exam = float(input("Escribe la calificación del examen: "))
a = float(input("Escribe la calificación del primer trabajo: "))
b = float(input("Escribe la calificación del segundo trabajo: "))
c = float(input("Escribe la calificación del tercer trabajo: "))

Tarea = (a + b + c) / 3
Pro_3 = (Exam * 0.85) + (Tarea * 0.15)

# Calcular el promedio general
Pro_General = (Pro_1 + Pro_2 + Pro_3) / 3

# Mostrar los promedios
print("=========================")
print("Tu promedio en Matemáticas es:", Pro_1)
print("Tu promedio en Física es:", Pro_2)
print("Tu promedio en Química es:", Pro_3)
print("Tu promedio General es:", Pro_General)
