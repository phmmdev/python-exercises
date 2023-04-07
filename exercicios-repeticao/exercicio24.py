import random


def main():

    grades = [random.randint(1, 10) for i in range(10)]
    total = sum(grades)
    average_grande = total / len(grades)

    print(f"notas : {grades}")
    print(f"a média das notas é: {average_grande}")


main()
