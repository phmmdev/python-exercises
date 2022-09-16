cars = []
kms = []


def get_cars_and_kms():
    for count in range(1, 6):
        print(f"Veículo {count}")
        cars.append(input("Nome: "))
        kms.append(float(input("Km por litro: ")))


def show_diff():
    print("Relatório Final ")
    for index, item in enumerate(cars):
        km_l = round(1000/kms[index], 2)
        km_l_price = round(km_l * 2.25, 2)
        print(f" {index} - {item}           -    {kms[index]} -  {km_l} litros - R$ {km_l_price}")


get_cars_and_kms()
show_diff()
