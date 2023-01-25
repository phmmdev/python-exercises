def main():
    values = get_values()
    get_classification(values)


def get_values():
    max_input = 10
    count = 1
    values = []
    while count <= max_input:
        values.append(int(input(f"({count}/{max_input}) informe um valor: ")))
        count += 1

    return values


def get_classification(values):
    odds = 0
    even = 0
    for number in values:
        if number % 2 == 0:
            odds += 1
        else:
            even += 1

    print(f"existem {odds} numeros pares e {even} numeros impares")


main()
