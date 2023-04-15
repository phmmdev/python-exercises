import random


def main():
    debts = round(random.uniform(500, 2500), 2)

    fees_parcels = [{"parcelas": 1, "juros": 0, "valor": debts}]
    fees = 10
    for i in  range(3, 13, 3):
        fees_parcels.append({"parcelas": i, "juros": fees, "valor": round(debts * (1+fees/100), 2)})
        fees += 5

    print("Valor da Dívida  ||  Valor dos Juros  ||  Quantidade de Parcelas ||   Valor da Parcela")
    for option in fees_parcels:
        print(f"R$ { option.get('valor') }  ||  {option.get('juros')}  ||  {option.get('parcelas')} ||  {round(option.get('valor') / option.get('parcelas'))} ")


main()