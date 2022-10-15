def main():
    strawberry_price = 2.50
    strawberry_discounted_price = 2.20
    apple_price = 1.80
    apple_discounted_price = 1.50
    price_limit = 25.00

    kg_limit = 5
    kg_total_limit = 8

    discount = 0.1

    strawberry_kg, apple_kg = get_values()
    fruit_total_kg = strawberry_kg + apple_kg

    strawberry_total_price = calculate_strawberry_price(strawberry_price, strawberry_discounted_price, strawberry_kg, kg_limit)
    apple_total_price = calculate_apple_price(apple_price, apple_discounted_price, apple_kg, kg_limit)

    total_price = calculate_discount(fruit_total_kg, kg_total_limit, strawberry_total_price, apple_total_price, price_limit, discount)

    print(f"""Maças: {apple_kg}Kg.......R${apple_total_price}
Morangos: {strawberry_kg}Kg.......R${strawberry_total_price}
Total:{total_price}""")


def get_values():
    strawberry_kg = float(input("informe quantos kilos de morango: "))
    apple_kg = float(input("informe quantos kilos de maçã: "))

    return strawberry_kg, apple_kg


def calculate_strawberry_price(strawberry_price, strawberry_discounted_price, strawberry_kg, kg_limit):
    return strawberry_price * strawberry_kg if strawberry_kg <= kg_limit else strawberry_discounted_price * strawberry_kg


def calculate_apple_price(apple_price, apple_discounted_price, apple_kg, kg_limit):
    return apple_price * apple_kg if apple_kg <= kg_limit else apple_discounted_price * apple_kg


def calculate_discount(total_kg, kg_total_limit, strawberry_total_price, apple_total_price, price_limit, discount):
    total_price = strawberry_total_price + apple_total_price
    if total_kg > kg_total_limit or total_price > price_limit:
        return total_price - (total_price * discount)
    else:
        return total_price


main()