def calc_fibonacci():
    anterior = 0
    proximo = 0

    while (proximo < 500):
        print(proximo)
        proximo = proximo + anterior
        anterior = proximo - anterior
        if (proximo == 0):
            proximo = proximo + 1


calc_fibonacci()