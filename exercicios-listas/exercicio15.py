import random


grades = []


def generate_grades_list():
    grade = 0
    while grade != -1:
        grade = random.randint(-1, 10)
        if grade != -1:
            grades.append(grade)


def get_grade_list_size():
    print(f"Tamanho da lista: {len(grades)}")


def get_grades():
    print(f"Notas: {grades}")


def get_reversed_grade_list():
    print(f"Notas Reversas: {grades[::-1]}")


def get_grades_total():
    print(f"Total Notas: {sum(grades)}")


def get_average_grades():
    average_grade = sum(grades) / len(grades)
    print(f"Média Notas: {average_grade}")
    return average_grade


def get_grades_greater_than_average(average_grade):
    filtered_grades = filter(lambda grade: grade >= average_grade, grades)
    print(f"Notas a cima da media: {list(filtered_grades)}")


def get_grades_smaller_than_average(average_grade):
    filtered_grades = filter(lambda grade: grade < average_grade, grades)
    print(f"Notas a baixo da media: {list(filtered_grades)}")


def finalization():
    print("Final da execução")


generate_grades_list()
get_grade_list_size()
get_grades()
average_grade = get_average_grades()
get_grades_greater_than_average(average_grade)
get_grades_smaller_than_average(average_grade)
finalization()

