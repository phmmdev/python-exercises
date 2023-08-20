def main():
    phone_number = input("informe um numero telefonico: ")
    if not has_correct_size(phone_number):
        phone_number = "3" + phone_number
        print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")

    if not has_separator(phone_number):
        print(f"Telefone corrigido sem formatação: {phone_number}")
        phone_number = phone_number[0:4] + "-" + phone_number[4:8]
        print(f"Telefone corrigido com formatação: {phone_number}")


def has_correct_size(phone_number):
    phone_number = phone_number.replace("-", "")
    return False if len(phone_number) != 8 else True


def has_separator(phone_number):
    return False if phone_number.count("-") == 0 else True


main()
