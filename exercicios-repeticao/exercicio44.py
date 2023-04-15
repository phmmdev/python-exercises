def main():
    candidates = generate_candidates_table()
    option = 'S'
    votes = []
    while option != 'N':
        print_candidates_table(candidates)
        votes.append(input("Informe seu voto: "))
        option = str.upper(input("Continuar [S/N]: "))

    for vote in votes:
        for candidate in candidates:
            if candidate.number == vote:
                candidate.votes += 1

    print_candidates_table(candidates, show_result=True)


def generate_candidates_table():
    candidates = [Candidate("Arthur", "1", 0),
                  Candidate("Bianca", "2", 0),
                  Candidate("Carlos", "3", 0),
                  Candidate("Daniele", "4", 0),
                  Candidate("Voto Nulo", "5", 0),
                  Candidate("Voto em Branco", "6", 0)]
    return candidates


def print_candidates_table(candidates, show_result=False):
    str_candidate = ''
    str_votes = ''
    for candidate in candidates:
        str_candidate = f"Número: {candidate.number}, Nome: {candidate.name}"
        str_votes = f"Votos: {candidate.votes}"
        if show_result:
            print(f"{str_candidate}, {str_votes}")
        else:
            print(f"{str_candidate}")


class Candidate:

    def __init__(self, name, number, votes):
        self.name = name
        self.number = number
        self.votes = votes


main()