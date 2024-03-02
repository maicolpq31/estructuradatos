"""Crear una lista de diccionarios donde cada diccionario contiene la información de un estudiante.

Usar un list comprehension para crear una lista de objetos de la clase Student a partir de la lista de diccionarios.

Usar otro list comprehension para filtrar los estudiantes, excluyendo los que tienen una nota promedio menor que un umbral dado.
Usar un dictionary comprehension para crear un diccionario de estudiantes que tienen una nota promeidio por encima de un umbral dado,
con los nombre de los estudiantes como claves y el objeto Student como valor."""
from Estructura_Datos.ejercicioclase import Student

#asi se crea un diccionario
data = [
    {"name": "Pedro", "age": 18, "grades": [2.6, 1.5, 4.2]},
    {"name": "Maria", "age": 23, "grades": [1.5, 3.8, 4.5]},
    {"name": "Sandro", "age": 19, "grades": [3.2, 3.8, 4.1]}
]

students: list[Student] = []
for register in data:
    student = Student(register["name"], register["age"]) #objeto estudiante
    for grade in register["grades"]:
        student.add_grade(grade)
    students.append(student)

for st in students:
    print(st)
