def convert_farenheit_to_celsius(temperature):
    converted_temperature = round(5 * ((temperature-32) / 9), 2)
    print(f"{temperature} em Farenheit é em Celsius: {converted_temperature}")


convert_farenheit_to_celsius(0)
convert_farenheit_to_celsius(60)
convert_farenheit_to_celsius(-7)
convert_farenheit_to_celsius(10)