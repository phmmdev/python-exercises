grades = []


def get_grades():
    while len(grades) < 4:
        value = int(input("informe um valor:"))
        grades.append(value)


def show_grades():
    print(f"Notas: {grades}")


def calculate_medium_grade():
    medium = sum(grades)/len(grades)
    print(f"A média de notas é: {medium}")


get_grades()
show_grades()
calculate_medium_grade()

