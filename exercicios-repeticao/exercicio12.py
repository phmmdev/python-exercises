def main():
    value = get_value()
    print_multiplication_table(value)


def get_value():
    value = int(input("informe o valor da tabuada desejava: "))
    return value


def print_multiplication_table(value):
    print(f"Tabuada de {value}:")
    for number in range(11):
        print(f"{value} X {number} = {value * number}")


main()