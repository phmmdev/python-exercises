def convert_celsius_to_farenheit(temperature):
    converted_temperature = round((temperature * 9/5) + 32, 2)
    print(f"{temperature} em Celsius é em Farenheit: {converted_temperature}")


convert_celsius_to_farenheit(0)
convert_celsius_to_farenheit(60)
convert_celsius_to_farenheit(-7)
convert_celsius_to_farenheit(10)