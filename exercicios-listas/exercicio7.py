numbers = [5, 8, 7, 6, 10]


def show_numbers():
    print(f"Numeros: {numbers}")


def shows_sum():
    print(f"Total Soma: {sum(numbers)}")


def shows_multiplication():
    total = 1
    for item in numbers:
        total *= item;

    print(f"Total Multiplicação: {total}")


show_numbers()
shows_sum()
shows_multiplication()