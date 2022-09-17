def convert_meters_to_centimeters(meters):
    if type(meters) == float and meters > 0.0:
        print(f"Convertendo {meters} em {meters * 100} centimetros")
    else:
        print("valores inválidos")


convert_meters_to_centimeters(0.5)
convert_meters_to_centimeters(2)
convert_meters_to_centimeters(3.3)