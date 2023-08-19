def main():
    width = fix_value(int(input("informe a largura do retangulo: ")))
    height = fix_value(int(input("informe a altura do retangulo: ")))

    draw(width, height)


def fix_value(value):
    if check_value(value):
        return value
    return 20


def check_value(value):
    if 1 <= value <= 20:
        return True
    return False


def draw(height, width):
    for i in range(height):
        if i == 0 or i == height - 1:
            line = "+" + (width -2)*"-" + "+"
            print(line)
        else:
            line = "|" + (width - 2) * " " + "|"
            print(line)


main()
