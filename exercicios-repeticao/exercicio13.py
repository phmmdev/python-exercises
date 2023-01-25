def main():
    values = get_values()
    print_result(values)


def get_values():
    values = []
    values.append(int(input("informe o primeiro valor: ")))
    values.append(int(input("informe o segundo valor: ")))

    return values


def print_result(values):
    result = values[0]
    pow = values[1]
    if values[1] == 0:
        result = 1
    elif values[1] < 0:
        pow = values[1] * -1

    count = 1
    while count <= pow -1:
        result = result * values[0]
        count += 1

    print(f"{values[0]} elevado a {values[1]} = {result}") if values[1] >= 0 else print(f"{values[0]} elevado a {values[1]} = 1/{result}")


main()
