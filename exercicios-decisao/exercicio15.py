def main():
    sides = [1, 2, 1]
    if check_triangle(sides):
        describe_triangle(sides)
    else:
        print("Lados não formam um triângulo")


def check_triangle(sides):
    if sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[1] + sides[2] >= sides[0]:
        return True

    return False


def describe_triangle(sides):
    if sides[0] == sides[1] == sides[2]:
        print("Triangulo Equilátero")
    elif sides[0] != sides[1] != sides[2] != sides[0]:
        print("Triangulo Escaleno")
    else:
        print("Triângulo Isósceles")


main()

