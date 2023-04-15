import random


def main():
    athletes = generate_athlete_list()
    for athlete in athletes:
        print(f"\nAtleta: {athlete.name}")
        print(f"Primeiro Salto: {athlete.jumps[0]}")
        print(f"Segundo Salto: {athlete.jumps[1]}")
        print(f"Terceiro Salto: {athlete.jumps[2]}")
        print(f"Quarto Salto: {athlete.jumps[3]}")
        print(f"Quinto Salto: {athlete.jumps[4]}")

        best_jump = max(athlete.jumps)
        worst_jump = min(athlete.jumps)
        avg_jump = round((sum(athlete.jumps) - (best_jump + worst_jump)) / 3, 2)

        print(f"\nMelhor Salto: {max(athlete.jumps)}")
        print(f"Pior Salto: {min(athlete.jumps)}")
        print(f"Média dos demais saltos: {avg_jump}")

        print("\nResultado final:")
        print(f"{athlete.name}: {avg_jump}")


def generate_athlete_list(number = 5):
    return [Athlete(f"Jumper{i}", generate_jumps()) for i in range(1, number + 1)]


def generate_jumps():
    return [round(random.uniform(1.2, 7.0), 2) for i in range(5)]

class Athlete:

    def __init__(self, name, jumps):
        self.jumps = jumps
        self.name = name


    def __repr__(self):
        return f"Nome: {self.name}, Saltos: {self.jumps}"


main()