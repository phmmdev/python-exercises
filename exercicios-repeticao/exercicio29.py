import random


class PriceTable:

    def __init__(self, number_itens, base_value):
        self.number_itens = number_itens
        self.base_value = base_value
        self.itens = []

    def generate(self):
        for i in range(1, self.number_itens + 1):
            value = round((self.base_value * i), 2)
            self.itens.append(f"{i} - R${value}")


price_table = PriceTable(50, 1.99)
price_table.generate()

print(price_table.itens)
