def main():
    values = get_values()
    print_interval(values)


def get_values():
    values = []
    values.append(int(input("Informe o primeiro valor: ")))
    values.append(int(input("Informe o segundo valor: ")))

    return values


def print_interval(values):
    interval = get_interval(values)

    for element in interval:
        print(f"{element}")


def get_interval(values):
    if values[0] < values[1]:
        interval = range(values[0], values[1] + 1, 1)
    else:
        interval = range(values[1], values[0] + 1, 1)

    return interval


main()