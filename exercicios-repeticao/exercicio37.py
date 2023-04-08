import random


def main():
    students = generate_students(15)
    gym = Gym(students)
    gym.get_taller()
    gym.get_smaller()
    gym.get_avg_height()
    gym.get_heavier()
    gym.get_lighter()
    gym.get_avg_weight()


def generate_students(quantity):
    return [Student(i, round(random.uniform(1.30, 2.00), 2), round(random.uniform(40, 180), 2)) for i in range(quantity)]


class Gym:
    def __init__(self, students):
        self.students = students

    def get_taller(self):
        taller = None
        for student in self.students:
            if taller is None:
                taller = student
            elif taller.height <= student.height:
                taller = student

        print(f"O menor aluno é: {taller}")

    def get_smaller(self):
        smaller = None
        for student in self.students:
            if smaller is None:
                smaller = student
            elif smaller.height >= student.height:
                smaller = student

        print(f"O menor aluno é: {smaller}")

    def get_avg_height(self):
        total = 0
        for student in self.students:
            total= total + student.height

        avg_height = round(total / len(self.students),2)
        print(f"A altura média é de: {avg_height}")

    def get_heavier(self):
        heavier = None
        for student in self.students:
            if heavier is None:
                heavier = student
            elif heavier.weight <= student.weight:
                heavier = student

        print(f"O menor aluno é: {heavier}")

    def get_lighter(self):
        lighter = None
        for student in self.students:
            if lighter is None:
                lighter = student
            elif lighter.weight >= student.weight:
                lighter = student

        print(f"O menor aluno é: {lighter}")

    def get_avg_weight(self):
        total = 0
        for student in self.students:
            total = total + student.weight

        avg_weight = round(total / len(self.students), 2)
        print(f"O peso médio é de: {avg_weight}")


class Student:
    def __init__(self, id, height, weight):
        self.id = id
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"Id: {self.id}, Altura: {self.height}, Peso: {self.weight} \n"


main()
