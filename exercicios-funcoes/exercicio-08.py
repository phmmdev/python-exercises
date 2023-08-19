def main():
    number = input("informe um numero inteiro: ")
    number_size = get_number_size(number)
    print(f"o numero informado contem {number_size} caracteres")


def get_number_size(number):
    return len(number)

main()