

d = {"abe": 1, "dfj": 1, "ghi": 3}

# for k in d:
#     print(d[k])   #valores del diccioanriao

# for k in ['medellín', 'ibague', 'bogota', 'cali']:
#     if "o" in k:
#         continue;
#     print(k)

# for i in ['medellín', 'ibague', 'bogota', 'cali']:
#     print(i)
# else:
#     print("FIN")

class Estudiante:
    def __init__(self, id, nombre, nota):
        self.id: int = id
        self.nombre : str = nombre
        self.nota: float = nota


class Curso:
    def __init__(self):
        self.estudiantes = []


    def agregar_estudiante(self, id, nombre, nota):
        self.estudiantes.append(Estudiante(id, nombre, nota))


    def notas_a_cero(self):
        for estudiante in self.estudiantes:
            if estudiante.nota > 3:
                break
            estudiante.nota = 0



    # def nota_mediana(self):
    #     return sum(self.estudiantes) / len(self.estudiantes)

curso = Curso()

curso.agregar_estudiante(5, "maico", 12121)
curso.agregar_estudiante(1, "Alice", 2.5)
curso.agregar_estudiante(2, "Bob", 3.2)
curso.agregar_estudiante(3, "Charlie", 1.8)
curso.agregar_estudiante(4, "David", 4.5)
curso.agregar_estudiante(5, "Eve", 0.5)

#nota_med = curso.nota_mediana()

print(curso.notas_a_cero())


