def main():
    try:
        number = int(input("informe um numero de 0 a 99, para ser escrito por extenso: "))
        spell_number(number)
    except:
        print("erro encontrado")


def spell_number(number):
    units = ["zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    tens = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    others = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

    text = ""
    if number < 10:
        text = units[number]
    if 10 < number < 20:
        text = tens[number - 10]
    else:
        index = number // 10
        unit = number - index * 10
        text = others[index - 2]
        if unit > 0:
            text += " e " + units[unit]

    print(text)

main()