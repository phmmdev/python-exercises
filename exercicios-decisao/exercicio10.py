def get_period():
    period = input("informe em qual período você estuda M-matutino ou V-Vespertino ou N- Noturno :")
    return period


def print_greetings(period):
    match period:
        case 'M':
            print("Bom dia !!")
        case 'V':
            print("Boa tarde !!")
        case "N":
            print("Boa noite !!")
        case _:
            print("Periodo inválido")


period = get_period()
print_greetings(period)
