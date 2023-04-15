import random


def main():
    students = generate_student_list()
    correct_answares = generate_answares()

    print(correct_answares)

    check_answares(students, correct_answares)

    for student in students:
        print(f"{student[0]}, {student[1]}, {student[3]}")


def generate_student_list(number=3):
    students = []
    for i in range(1, number + 1):
        students.append([i, generate_answares(), [], 0])

    return students


def generate_answares():
    return [random.choice(['A', 'B', 'C', 'D', 'E']) for i in range(10)]


def check_answares(students, correct_answares):
    for student in students:
        student[2] = list(map(lambda x, y: (x, y, x == y), student[1], correct_answares))
        student[3] = len(list(filter(lambda x: x[2], student[2])))


main()
