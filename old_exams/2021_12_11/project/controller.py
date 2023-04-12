from typing import List
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class CarFactory:
    valid_type_cars = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    @staticmethod
    def create_car(car_type, model, speed_limit ):
        return CarFactory.valid_type_cars[car_type](model, speed_limit)


class DriverFactory:
    @staticmethod
    def create_driver(driver_name):
        return Driver(driver_name)


class RaceFactory:
    @staticmethod
    def create_race(race_name):
        return Race(race_name)


class Controller:
    def __init__(self):
        self.cars: List = []        # empty list that will contain all cars (objects)
        self.drivers: List = []     # empty list that will contain all drivers (objects)
        self.races: List = []       # empty list that will contain all races (objects)

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if [c for c in self.cars if c.model == model]:
            raise Exception(f"Car {model} is already created!")

        if car_type in CarFactory.valid_type_cars:
            car = CarFactory.create_car(car_type, model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if [d for d in self.drivers if d.name == driver_name]:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = DriverFactory.create_driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if [r for r in self.races if r.name == race_name]:
            raise Exception(f"Race {race_name} is already created!")

        race = RaceFactory.create_race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if not [d for d in self.drivers if d.name == driver_name]:
            raise Exception(f"Driver {driver_name} could not be found!")
        driver = self.__find_driver_by_name(driver_name)

        if not [c for c in self.cars if c.__class__.__name__ == car_type and not c.is_taken]:
            raise Exception(f"Car {car_type} could not be found!")
        car = [c for c in self.cars if c.__class__.__name__ == car_type and not c.is_taken][-1]
        car.is_taken = True

        if driver.car:
            old_car = driver.car
            old_car.is_taken = False
            driver.car = car
            return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."
        driver.car = car
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not [r for r in self.races if r.name == race_name]:
            raise Exception(f"Race {race_name} could not be found!")

        if not [d for d in self.drivers if d.name == driver_name]:
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = self.__find_driver_by_name(driver_name)
        race = self.__find_race_by_name(race_name)

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        if not [r for r in self.races if r.name == race_name]:
            raise Exception(f"Race {race_name} could not be found!")

        race = self.__find_race_by_name(race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        sorted_drivers = sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True)
        # sorted_drivers = sorted(race.drivers, key=lambda x: (-x.car.speed_limit, x.name))

        top_3_drivers = []
        for driver in sorted_drivers[0:3]:
            driver.number_of_wins += 1
            top_3_drivers.append(f"Driver {driver.name} wins the {race_name}"
                                 f" race with a speed of {driver.car.speed_limit}.")

        top_3_drivers_return = "\n".join(top_3_drivers)
        return top_3_drivers_return

    def __find_race_by_name(self, name):
        return [r for r in self.races if r.name == name][0]

    def __find_driver_by_name(self, name):
        return [d for d in self.drivers if d.name == name][0]
