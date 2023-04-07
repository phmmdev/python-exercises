import random


class CD:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"Name: {self.name}, Value: {self.value}"


class Inventory():

    def __init__(self, cd_list=None):
        if cd_list is None:
            self.cd_list = []

    def exec(self):
        exit = False
        while not exit:
            name = input("informe o nome do CD ")
            value = float(input("informe o valor do CD "))
            self.cd_list.append(CD(name, value))
            exit = True if input("informar mais CDs ? [S/N] ").upper() == 'N' else False

        for cd in self.cd_list:
            print("-- "+str(cd))

        print("calculando valor médio da coleção ....")
        print(f"O valor médio é {self.calc_average_value()}")

    def calc_average_value(self):
        if len(self.cd_list) == 0:
            return 0

        total = 0
        for cd in self.cd_list:
            total += cd.value

        return round(total / len(self.cd_list))


inventory = Inventory()

inventory.exec()
