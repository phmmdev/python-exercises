def get_price():
    first_price = float(input("informe o valor do primeiro produto "))
    second_price= float(input("informe o valor do segundo produto"))
    third_price = float(input("informe o valor do terceiro produto "))

    return first_price, second_price, third_price


def get_smaller_price(first_price, second_price, third_price):
    if first_price <= second_price and first_price <= third_price:
        print(f"O primeiro valor é menor : {first_price}")
    elif second_price <= first_price and second_price <= third_price:
        print(f"O segundo valor é menor : {second_price}")
    else:
        print(f"O terceiro valor é menor : {third_price}")


first_price, second_price, third_price = get_price()
get_smaller_price(first_price, second_price, third_price)