def main():
    inputs = get_values()
    results =  execute_operation(inputs)
    show_results(results)


def get_values():
    inputs = []
    numbers = input("informe dois numeros").split(",")
    inputs.append(numbers)
    operation = input("informe qual operação deseja realizar (+, -, *, /)")
    inputs.append(operation)
    return inputs


def execute_operation(inputs):
    if inputs[1] == "+":
        return float(inputs[0][0]) + float(inputs[0][1])
    if inputs[1] == "-":
        return float(inputs[0][0]) - float(inputs[0][1])
    if inputs[1] == "*":
        return float(inputs[0][0]) * float(inputs[0][1])
    if inputs[1] == "/":
        return float(inputs[0][0]) / float(inputs[0][1])


def show_results(results):
    if check_decimal_alternative(results):
        print("Numero decimal")
    else:
        print("Numero inteiro")

    if is_odd(results):
        print("Numero par")
    else:
        print("Numero impar")

    if is_positive(results):
        print("Numero positivo")
    else:
        print("Numero negativo")


def check_decimal_alternative(number):
    rounded_number = round(number)
    return True if number != rounded_number else False


def is_odd(number):
    return True if number % 2 == 0 else False


def is_positive(number):
    return True if number >= 0 else False


main()