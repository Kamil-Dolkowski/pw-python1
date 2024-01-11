import logging

logging.basicConfig(filename='car.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Car:

    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__is_production = False

    def start_production(self):
        if not self.__is_production:
            # print(f"Rozpoczęcie produkcji {self.__make} {self.__model} {self.__year}")
            logging.info(f"Rozpoczęcie produkcji {self.__make} {self.__model} {self.__year}")
            self.__is_production = True
        else:
            # print("Aktualnie jest produkowany.")
            logging.warning("Aktualnie jest produkowany.")
    
    def stop_production(self):
        if self.__is_production:
            # print(f"Zatrzymanie produkcji {self.__make} {self.__model} {self.__year}")
            logging.info(f"Zatrzymanie produkcji {self.__make} {self.__model} {self.__year}")
            self.__is_production = False
        else:
            # print("Aktualnie nie jest produkowany.")
            logging.warning("Aktualnie nie jest produkowany.")

    def display_info(self):
        # print(f"Marka: {self.__make}")
        # print(f"Model: {self.__model}")
        # print(f"Rok produkcji: {self.__year}")
        # print(f"Czy jest aktualnie produkcja? {'Tak' if self.__is_production else 'Nie'}")
        logging.info(f"Marka: {self.__make}")
        logging.info(f"Model: {self.__model}")
        logging.info(f"Rok produkcji: {self.__year}")
        logging.info(f"Czy jest aktualnie produkcja? {'Tak' if self.__is_production else 'Nie'}")


class ElectricalCar(Car):       # dziedziczenie - przejmuje parametry

    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.__battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        # print(f"Pojemność baterii: {self.__battery_capacity} kWh")
        logging.info(f"Pojemność baterii: {self.__battery_capacity} kWh")





def main():
    car = Car("Toyota","Camry",2023)
    electric_car = ElectricalCar("Tesla", "Model 3", 2024, 75)

    car.display_info()
    car.start_production()
    car.stop_production()

    electric_car.display_info()
    electric_car.start_production()
    electric_car.stop_production()

if __name__ == "__main__":
    main()

