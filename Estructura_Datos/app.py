"""
"""
from Estructura_Datos.ejercicioclase import Student

#Crear una lista de diccionarios donde cada diccionario contiene la información de un estudiante.

#asi se crea un diccionario,  una lista adentro las claves: y valores
data = [
    {"name": "Pedro", "age": 18, "grades": [3.3, 4.1, 5]},
    {"name": "Maria", "age": 23, "grades": [3.4, 3.8, 4.5]},
    {"name": "Sandro", "age": 19, "grades": [3.2, 3.8, 4.1]}
]

#Usar un list comprehension para crear una lista de objetos de la clase Student a partir de la lista de diccionarios.

students: list[Student] = []      #Hacerlo en listcomprehention
for register in data:
    student = Student(register["name"], register["age"]) #objeto estudiante
    for grade in register["grades"]:
        student.add_grade(grade)
    students.append(student)

threshold = 3.9#limite del promedio mostrado en pantalla

for st in students:
    print(st)

#Usar otro list comprehension para filtrar los estudiantes, excluyendo los que tienen una nota promedio menor que un umbral dado.
filtered_students: list[Student] = [st for st in students if st.average_grade() >= threshold]

# for st in students:
#     if st.average_grade() >= threshold:
#         filtered_students.append(st)


#Usar un dictionary comprehension para crear un diccionario de estudiantes que tienen una nota promedio por encima de un umbral dado, con los nombre de los estudiantes como claves y el objeto Student como valor.
#dict_students: dict[str, Student] = {}
#for st in students:
#    if st.average_grade() >= threshold:
#        dict_students[st.name] = st
dc_dict_students = {st.name: st for st in students if st.average_grade() >= threshold}

print("\nDICCIONARIO DE ESTUDIANTES")
print(dc_dict_students)


print(f"Students with average grade over {threshold}")
for st in filtered_students:
    print(st)