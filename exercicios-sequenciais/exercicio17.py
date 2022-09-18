import math


def calculate_ink(meters):
    total_ink = (meters / 6) * 1.1
    can = total_ink / 18
    gallons = total_ink / 3.6

    excess_can = (can - math.floor(can)) * 18
    excess_gallon = excess_can / 3.6

    return math.ceil(can), math.ceil(gallons), math.floor(can),  math.ceil(excess_gallon)


def calculate_total(can, gallons, excess_can, excess_gallon):
    total_can = round(can * 80.00, 2)

    print(f"\n  {'-' * 10} Galões {'-' * 10}")
    print(f"A quantidade de latas a serem compradas é de: {can}")
    print(f"O valor total a ser pago é de: {total_can}")


    total_gallons = round(gallons * 25.00, 2)

    print(f"\n {'-' * 10} Latas {'-' * 10}")
    print(f"A quantidade de galões a serem comprados é de: {gallons}")
    print(f"O valor total a ser pago é de: {total_gallons}")

    total_excess_can = round(excess_can * 80.00, 2)
    total_excess_gallons = round(excess_gallon * 25.00, 2)

    print(f"\n {'-' * 10} MISTO - Galões e Latas {'-' * 10}")
    print(f"A quantidade de latas a serem compradas é de: {excess_can}")
    print(f"A quantidade de galões a serem comprados é de: {excess_gallon}")
    print(f"O valor total a ser pago é de: {total_excess_can + total_excess_gallons}")


can, gallons, excess_can, excess_gallon = calculate_ink(200)
calculate_total(can, gallons, excess_can, excess_gallon)
