def calc_fatorial(nvalue):
    if nvalue == 0:
        return print(1)

    total = 1;
    while (nvalue > 1):
        total *= nvalue
        nvalue -=1

    print(total)


def main():
    valor = 0
    while valor != -1:
        valor = int(input("Informe o valor Fatorial deseja calcular, -1 para sair"))
        if valor > 15:
            print("O valor informado deve ser menor que 16")
        elif valor != -1:
            calc_fatorial(valor)


main()