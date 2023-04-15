def main():
    option = "S"
    menu = generate_menu()
    order = []
    while option != "N":
        print(menu)
        code = input("informe o produto: ")
        qtd = int(input("informe  a quantidade"))
        option = str.upper(input("Deseja continuar o pedido [S/ N]"))
        order.append([code, qtd, 0])

    for item in order:
        product = dict(list(filter(lambda x: x.get("codigo") == item[0], menu))[0])
        item[2] = round(float(product.get("valor")) * float(item[1]), 2)
        print(f"Item: {product.get('produto')} .... {product.get('valor')} x {item[1]} = {item[2]}")

    total = round(sum(item[2] for item in order), 2)
    print(f"Total: {total}")


def generate_menu():
    return [{"produto": "Cachorro Quente", "codigo": "100", "valor": "1.20"},
            {"produto": "Bauru Simples", "codigo": "101", "valor": "1.30"},
            {"produto": "Bauru com ovo", "codigo": "102", "valor": "1.50"},
            {"produto": "Hambúrguer", "codigo": "103", "valor": "1.20"},
            {"produto": "Cheeseburguer", "codigo": "104", "valor": "1.30"},
            {"produto": "Refrigerante", "codigo": "105", "valor": "1.00"}, ]

main()