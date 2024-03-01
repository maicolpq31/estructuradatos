"""Crear una clase Student que tiene los siguientes atributos: name, age y grades (una lista de números)
Crear un constructor que inicialice los atributos

Crear un método llamado add_grade que recibe un número como parámetro y lo agrega a la lista grades.

Crear otro método llamado average_grade que calcule y retorne la nota promedio de la lista de notas grades
Crear una lista de diccionarios donde cada diccionario contiene la información de un estudiante.
Usar un list comprehension para crear una lista de objetos de la clase Student a partir de la lista de diccionarios.
Usar otro list comprehension para filtrar los estudiantes, excluyendo los que tienen una nota promedio menor que un umbral dado.
Usar un dictionary comprehension para crear un diccionario de estudiantes que tienen una nota promeidio por encima de un umbral dado,
con los nombre de los estudiantes como claves y el objeto Student como valor."""

class Student:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
        self.grades: list[float] = []


    def add_grade(self, grade: float):
        self.grades.append(grade)


    def average_grade(self) -> float:
        return sum(self.grades) / len(self.grades)

