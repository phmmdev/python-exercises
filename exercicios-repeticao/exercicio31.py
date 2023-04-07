class CashMachine:

    def __init__(self, product_list, payment_value):
        if product_list is None:
            self.product_list = []
        else:
            self.product_list = product_list

        self.payment_value = payment_value

    def calc_total(self):
        total = 0
        for product_value in self.product_list:
            total += product_value
        return total

    def calc_change(self, total):
        return self.payment_value - total

    def return_resume(self):
        print("Lojas Tabajara")
        for i, produto in enumerate(self.product_list):
            print("Produto")
            print(f"{i+1}: R$ {produto}")

        total = self.calc_total()
        print(f"Total: R$ {total}")
        print(f"Dinheiro: R$ {self.payment_value}")
        print(f"Troco: R$ {self.calc_change(total)}")


cashMachine = CashMachine([2.20, 5.80], 20.00)
cashMachine.return_resume()
