import random


class Main:
    @staticmethod
    def main():
        class_quantity = 5
        student_max_quantity = 40

        classes = [Class(f"classe-{i}", random.randint(1, student_max_quantity)) for i in range(5)]

        total_students = 0
        for _class in classes:
            print(_class)
            total_students = total_students + _class.students_quantity

        average_students_class = total_students / class_quantity

        print(f"a média de alunos por classe é de {average_students_class}")
        

class Class:

    def __init__(self, class_name, students_quantity):
        self.class_name = class_name
        self.students_quantity = students_quantity

    def __str__(self):
        return f"{self.class_name}, {self.students_quantity}"

Main.main()