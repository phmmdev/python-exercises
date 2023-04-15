def main():
    input_value = 0
    ranges_values = {"[0-25]": [0, 25, 0],
                     "[26-50]": [26, 50, 0],
                     "[51-75]": [51, 75, 0],
                     "[76-100]": [76, 100, 0]
                     }

    while input_value >= 0:
        input_value = int(input("informe um valor de 0 - 100: "))

        for k, v in ranges_values.items():
            if v[0] <= input_value <= v[1]:
                v[2] = v[2] + 1
            print(k, v)

    print("Resultado: ")

    for range in ranges_values.items():
        print(f"{range[0]} -- {range[1]}")


main()
