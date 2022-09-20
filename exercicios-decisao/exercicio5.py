def get_grades():
    first_grade = int(input("informe o primeiro nota "))
    second_grade = int(input("informe o segunda nota "))
    return first_grade, second_grade


def get_average_grade(first_grade, second_grade):
    average_grade = (first_grade + second_grade) / 2
    return average_grade


def get_grades_result(average_grades):
    if average_grades == 10:
        print("Aprovado com Distinção")
    elif average_grades >= 7:
        print("Aprovado")
    else:
        print("Reprovado")


first_grade, second_grade = get_grades()
average_grade = get_average_grade(first_grade, second_grade)
get_grades_result(average_grade)
