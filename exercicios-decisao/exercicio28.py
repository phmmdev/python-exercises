def main():
    price_table = [["1", "File Duplo", 4.90, 5.80], ["2", "Alcatra", 5.90, 6.80], ["3", "Picanha", 6.90, 7.80]]
    kg_limit = 5
    discount = 0.05

    selected_option, kg, has_card = get_values(price_table)
    item, total_price, discount_value = calculate_total_price(selected_option, kg, has_card, price_table, kg_limit, discount)

    print(f"Opção Selecionada: {item[0]} - {item[1]}")
    print(f"Quantidades de kilos: {kg}")
    print(f"Cartão fidelidade: {has_card}")
    print(f"Desconto: {discount_value}")
    print(f"Total a pagar: {total_price}")


def get_values(price_values):
    print("Opção .............. Corte ............. Até 5kg ............... Acima de 5Kg")
    for item in price_values:
        print(f"{item[0]} ........ {item[1]} .......... {item[2]} .......... {item[3]}")

    selected_option = input("informe o tipo de corte: ")
    kg = float(input("informe a quantidade de kilos: "))
    has_card = input("possui cartão fidelidade? (S/N): ")

    return selected_option, kg, has_card


def calculate_total_price(selected_option, kg, has_card, price_table, kg_limit, discount):
    option = [item for item in price_table if item[0] == selected_option][0]
    total_price = kg * option[2] if kg < kg_limit else kg * option[3]

    discount_value = round(total_price * discount, 2)

    total_price = total_price - discount_value if has_card == "S" else total_price
    return option, total_price, discount_value


main()