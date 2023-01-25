def main():
    values = get_values()
    get_values_sum(values)
    get_values_average(values)


def get_values():
    max_input = 5
    count = 1
    values = []
    while count <= max_input:
        values.append(int(input(f"({count}/{max_input}) informe um valor: ")))
        count += 1

    return values


def get_values_sum(values):
    total = sum(values)
    print(f"A soma dos valores é: {total}")


def get_values_average(values):
    average = sum(values)//5
    print(f"A média dos valores é: {average}")


main()
