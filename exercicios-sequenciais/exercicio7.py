def calculate_square_area(side):
    if side > 0:
        area = side**2
        print(f"A áre ado quadro de lado {side}, é de {area}")
        print(f"O dobro da áre é de {area * 2}")
    else:
        print(f"valaores inválidos")


calculate_square_area(4)
calculate_square_area(2)
calculate_square_area(6)