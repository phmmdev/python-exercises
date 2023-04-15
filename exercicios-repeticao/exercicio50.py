def main():
    serie = ''
    for i in range(1, 11):
        serie = serie + f"1/{i} + "

    print(serie[0:-2])


main()