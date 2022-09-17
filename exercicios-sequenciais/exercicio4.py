def get_grades():
    total = 0
    for count in range(1, 5):
        total += int(input(f"informe a nota {count}: "))

    average_grade = total / 4
    print(f"a média é: {average_grade}")


get_grades()
