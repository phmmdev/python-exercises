def main():
    name = input("informe seu nome: ")
    name_size = len(name)
    for i in range(name_size):
        print(name)
        name = name[:-1]


main()
