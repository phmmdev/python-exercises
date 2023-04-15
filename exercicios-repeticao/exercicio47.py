import random


def main():
    athletes = generate_athlete_list()
    for athlete in athletes:
        print(f"\nAtleta: {athlete.name}")
        for grade in athlete.grades:
            print(f"Nota: {grade}")

        best_grade = max(athlete.grades)
        worst_grade = min(athlete.grades)
        avg_grade = round((sum(athlete.grades) - (best_grade + worst_grade)) / 7, 2)

        print("\nResultado final:")
        print(f"Atleta: {athlete.name}")
        print(f"Melhor nota: {best_grade}")
        print(f"Pior nota: {worst_grade}")
        print(f"Média das notas: {avg_grade}")


def generate_athlete_list(number = 5):
    return [Athlete(f"Atleta-{i}", generate_grades()) for i in range(1, number + 1)]


def generate_grades():
    return [round(random.uniform(0.0, 10.0), 2) for i in range(7)]


class Athlete:

    def __init__(self, name, grades):
        self.grades = grades
        self.name = name


    def __repr__(self):
        return f"Nome: {self.name}, Saltos: {self.grades}"


main()