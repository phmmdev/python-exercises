import random


class City:

    def __init__(self, id, cars, car_accident):
        self.id = id
        self.cars = cars
        self.car_accident = car_accident

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


def main():
    cities = generate_cities()
    max_accident_ocurrency = get_city_max_car_accident_ocurrency(cities)
    min_accident_ocurrency = get_city_min_car_accident_ocurrency(cities)
    average_cars_quantities = get_avg_cars_quantities(cities)
    average_accidents_filter_by_cars = get_average_accidents_filter_by_cars(cities)

    print(f" LISTA DAS CIDADES: {cities}")
    print(f" CIDADE COM MAIS ACIDENTES: {max_accident_ocurrency}")
    print(f" CIDADE COM MENOS ACIDENTES: {min_accident_ocurrency}")
    print(f" QTD. MÉDIA DE CARROS: {average_cars_quantities}")
    print(f" QTD. MÉDIA DE ACIDENTES: {average_accidents_filter_by_cars}")


def generate_cities():
    return [City(i, random.randint(500, 2500), random.randint(0, 1000)) for i in range(5)]


def get_city_max_car_accident_ocurrency(cities):
    return max(cities, key=lambda x: x.car_accident)


def get_city_min_car_accident_ocurrency(cities):
    return min(cities, key=lambda x: x.car_accident)


def get_avg_cars_quantities(cities, number_cities=5):
    return round(sum(city.cars for city in cities) / number_cities, 2)


def get_average_accidents_filter_by_cars(cities):
    filtered_cities = list(filter(lambda city: city.cars < 2000, cities))
    if len(filtered_cities) > 0:
        avg_accidents = round(sum(city.car_accident for city in filtered_cities) / len(filtered_cities), 2)
        return avg_accidents
    else:
        return 0

main()
