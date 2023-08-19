def price_plus_taxes(tax, price):
    return price + round(price * (tax / 100), 2)


print(price_plus_taxes(10,10))
print(price_plus_taxes(20,5))
print(price_plus_taxes(30,15))
print(price_plus_taxes(100,25))
