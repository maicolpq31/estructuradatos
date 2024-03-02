




"""Crear una clase Student que tiene los siguientes atributos: name, age y grades (una lista de números)
Crear un constructor que inicialice los atributos"""
class Student:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
        self.grades: list[float] = []

    """Crear un método llamado add_grade que recibe un número como parámetro y lo agrega a la lista grades."""
    def add_grade(self, grade: float):   #grade = calificacion
        self.grades.append(grade)

    """Crear otro método llamado average_grade que calcule y retorne la nota promedio de la lista de notas grades"""
    def average_grade(self) -> float:
        return sum(self.grades) / len(self.grades)

    #metodo especial para printear esos resultados
    def __str__(self):
        return f"{self.name}, edad {self.age}, -promedio {self.average_grade()}"

