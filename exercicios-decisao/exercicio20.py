def main(grade1, grade2, grade3):
    average = get_average_grades(grade1, grade2, grade3)
    check_grades(average)


def get_average_grades(grade1, grade2, grade3):
    return round((grade1 + grade2 + grade3) / 3, 2)


def check_grades(average_grade):
    if average_grade == 10:
        print(f"Aprovado com Distinção - {average_grade}")
    elif average_grade >= 7:
        print(f"Aprovado - {average_grade}")
    else:
        print(f"Repovado - {average_grade}")


main(10, 10, 10)
main(8, 7, 9)
main(5, 7, 4)