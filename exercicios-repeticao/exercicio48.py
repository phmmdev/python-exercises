import random


def main():
    number = generate_number()
    reversed_number = number[::-1]
    print(f"Número: {number}")
    print(f"Número Invertido: {reversed_number}")


def generate_number():
    return str(random.randint(0, 10_000_000))


main()