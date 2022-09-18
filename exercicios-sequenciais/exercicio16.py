import math


def calculate_ink(meters):
    total_ink = meters / 3
    ink_gallons = math.ceil(total_ink / 18)

    if ink_gallons < 1:
        ink_gallons = 1

    return ink_gallons


def calculate_total(ink_gallons):
    total = round(ink_gallons * 80.00, 2)
    print(f"A quantidade de latas a serem compradas é de: {ink_gallons}")
    print(f"O valor total a ser pago é de: {total}")


gallons = calculate_ink(180)
calculate_total(gallons)