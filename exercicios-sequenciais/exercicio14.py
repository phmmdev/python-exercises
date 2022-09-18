def calcute_taxes(fish_weight):
    excess = fish_weight - 50
    if excess > 0:
        taxes = excess * 4.00
        print(f"Foram excedidos {excess} e deve ser pago R$ {taxes} de multa")
    else:
        print(f"Peso adequado, não há multas")


calcute_taxes(100)
calcute_taxes(50)
calcute_taxes(10)

