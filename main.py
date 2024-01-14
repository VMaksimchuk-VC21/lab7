class TransportCompany:
    def __init__(self, name):
        self.__name = name
        self.__vehicles = []

    @property
    def name(self):
        return self.__name

    @property
    def vehicles(self):
        return self.__vehicles

    def __str__(self):
        return f"Фирма: {self.name}"

    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)


class Vehicle:
    def __init__(self, model, company):
        self.__model = model
        self.__company = company
        self.__drivers = []

    @property
    def model(self):
        return self.__model

    @property
    def company(self):
        return self.__company

    @property
    def drivers(self):
        return self.__drivers

    def __str__(self):
        return f"Транспорт: {self.model} ({self.company.name})"

    def add_driver(self, driver):
        self.__drivers.append(driver)


class Driver:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"Водитель: {self.name}"



def create_company():
    name = input("Введите название фирмы: ")
    return TransportCompany(name)


def create_vehicle(company):
    model = input("Введите модель транспорта: ")
    return Vehicle(model, company)


def create_driver():
    name = input("Введите имя водителя: ")
    return Driver(name)

