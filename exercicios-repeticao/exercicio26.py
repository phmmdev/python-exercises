import random


def main():
    candidates = (["Candidato-1", 0], ["Candidato-2", 0], ["Candidato-3", 0])

    voters = 20
    for i in range(20):
        vote = random.randint(0, 2)
        candidates[vote][1] = candidates[vote][1] + 1


    print("o resultado das eleições foram: ")

    for candidate in candidates:
        print(f"Nome: {candidate[0]}, Votos: {candidate[1]}, Percentual: {(candidate[1] / voters) * 100}%")


main()


