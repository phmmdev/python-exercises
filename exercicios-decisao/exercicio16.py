import math


def main():
    a_value, b_value, c_value = get_values()
    if not valid_values(a_value):
        print("A equação não é do segundo grau")
    else:
        delta = calculate_delta(a_value, b_value, c_value)
        show_results(a_value, b_value, delta)


def get_values():
    a_value = int(input('Digite o valor de a: '))
    b_value = int(input('Digite o valor de b: '))
    c_value = int(input('Digite o valor de c: '))

    return a_value, b_value, c_value


def valid_values(a_value):
    return a_value != 0


def calculate_delta(a_value, b_value, c_value):
    delta = (b_value**2) - (4 * a_value * c_value)
    return delta


def calculate_two_squares(a_value, b_value, delta):
    square1 = (-b_value + math.sqrt(delta)) / (2 * a_value)
    square2 = (-b_value - math.sqrt(delta)) / (2 * a_value)
    return square1, square2


def calculate_one_squares(a_value, b_value, delta):
    square1 = -b_value / (2 * a_value)

    return square1


def show_results(a_value, b_value, delta):
    if delta < 0:
        print(f"O valor de delta é negativo: {delta}")
    elif delta == 0:
        square1 = calculate_one_squares(a_value, b_value, delta)
        print(f'A equação possui uma raiz real: {delta}, raiz x1: {square1}')
    else:
        square1, square2 = calculate_two_squares(a_value, b_value, delta)
        print(f'A equação possui duas raizes reais, {delta}, raiz x1:  {square1} raiz x2:  {square2}')


main()
