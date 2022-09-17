def calculate_values(number1, number2, number3):
    if type(number1) == int and type(number2) == int and type(number3) == float:
        first_result = (number1 * 2) * (number2 // 2)
        second_result = (number1 * 3) * number3
        third_result = round(number3**3, 2)

        print(f"""Primeiro resultado: {first_result}
Segundo resultado: {second_result}
Terceiro resultado: {third_result}""")


calculate_values(10, 10, 2.5)
calculate_values(5, 7, 7.8)
calculate_values(2, 8, 3.9)