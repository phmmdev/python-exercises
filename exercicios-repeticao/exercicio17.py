def calc_fatorial(nvalue):
    if nvalue == 0:
        return print(1)

    total = 1;
    while (nvalue > 1):
        total *= nvalue
        nvalue -=1

    print(total)

calc_fatorial(5)