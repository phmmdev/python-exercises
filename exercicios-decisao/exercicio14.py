def get_grades():
    grades = input("informe duas notas: ").split()
    return grades


def get_average_grade(grades):
    return round(((float(grades[0]) + float(grades[1])) / 2), 2)


def classify_grades(average_grade):
    grade_description = ""
    if 9.00 < average_grade <= 10.0:
        grade_description = "A"
    elif 7.5 < average_grade <= 9.0:
        grade_description = "B"
    elif 6.0 < average_grade <= 7.5:
        grade_description = "C"
    elif 4.0 < average_grade <= 6.0:
        grade_description = "D"
    elif 0.0 < average_grade <= 4.0:
        grade_description = "E"

    print(f"Nota: {average_grade}, Conceito: {grade_description}")

    return grade_description


grades = get_grades()
average_grade = get_average_grade(grades)
classify_grades(average_grade)
