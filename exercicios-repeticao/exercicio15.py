def calc_fibonacci(nvalue):
    anterior = 0
    proximo = 0

    while (nvalue != 0):
        print(proximo)
        proximo = proximo + anterior
        anterior = proximo - anterior
        if (proximo == 0):
            proximo = proximo + 1

        nvalue -= 1


calc_fibonacci(5)
calc_fibonacci(8)