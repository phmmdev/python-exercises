def main():
    value = get_values()
    print(f"O valor informado é : {value}")


def get_values():
    value = -1
    while value not in range(0,11):
        value = int(input("informe um valor entre 0 e 10"))

    return value


main()
