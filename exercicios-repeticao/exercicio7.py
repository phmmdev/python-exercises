def main():
    values = get_values()
    get_biggest_value(values)


def get_values():
    max_input = 5
    count = 1
    values = []
    while count <= max_input:
        values.append(int(input(f"({count}/{max_input}) informe um valor: ")))
        count += 1

    return values


def get_biggest_value(values):
    biggest = max(values)
    print(f"O maior valor é {biggest}")


main()