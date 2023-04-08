import random


def main():
    number_max = 10
    number = random.randint(1, number_max)
    start = random.randint(1, number_max)
    end = random.randint(start, number_max)

    print(f"Montar a tabuada de: {number}")
    print(f"Começar por: {start}")
    print(f"Termina em: {end}")

    print(f"Vou montar a tabuada de {number} começando em {start} e terminando em {end}: ")

    for i in range(start, end+1):
        print(f"{number} X {i} = {number * i}")


main()

