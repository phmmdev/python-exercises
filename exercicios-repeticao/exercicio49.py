def main():
    j = 1
    serie = ''
    soma = 0
    for i in range(1,11):
        serie = serie + f"{i}/{j} + "
        j += 2
        soma += i/j

    print(serie[0:-2])
    print(f"Soma: {round(soma, 2)}")

main()