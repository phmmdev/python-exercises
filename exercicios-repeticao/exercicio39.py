import random

def main():
    students = []
    for i in range(1, 21):
        students.append((i, random.randint(120, 175)))

    get_smaller(students)
    get_higher(students)


def get_smaller(students):
    smaller = ()
    for student in students:
        if len(smaller) == 0:
            smaller = student
        elif smaller[1] >= student[1]:
            smaller = student

    print(f"O menor aluno é: {smaller}")


def get_higher(students):
    higher = ()
    for student in students:
        if len(higher) == 0:
            higher = student
        elif higher[1] <= student[1]:
            higher = student

    print(f"O maior aluno é: {higher}")


main()