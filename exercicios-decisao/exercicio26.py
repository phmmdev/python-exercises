def main():
    fuel_type, litres = get_values()
    total = get_total_price(fuel_type, float(litres))
    show_result(total)


def get_values():
    fuel_type = input("informe o combustível (G- Gasolina, A- Alcool)")
    litres = input("informe a quantos litros")

    return fuel_type, litres


def get_total_price(fuel_type, litres):
    total = 0
    if fuel_type == "A":
        total = litres * 1.90
        if litres <= 20:
            total = total - (total * 0.03)
        else:
            total = total - (total * 0.05)
    else:
        total = litres * 2.50
        if litres <= 20:
            total = total - (total * 0.04)
        else:
            total = total - (total * 0.06)

    return total


def show_result(total):
    print(f"valor total a pagar {total}")


main()