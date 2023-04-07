import random
def main():

    people = [(random.randint(1, 100), f"person-{i}") for i in range(3)]
    ages = 0
    [ages := ages + person[0] for person in people]

    average_age = ages // len(people)

    print(f"pessoas : {people}")

    print(f"a média de idade é {average_age}")

    if 0 < average_age <= 25:
        print("Turma Jovem")
    elif 26 < average_age <= 60:
        print("Turma Adulta")
    else:
        print("Turma Idosa")


main()
