from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def refuel(self, fuel: float):
        pass

    def drive_on(self, distance, consumption):
        needed_fuel = (self.fuel_consumption + consumption) * distance
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel


class Car(Vehicle):
    conditioner_add_fuel = 0.9

    def drive(self, distance) -> None:
        Vehicle.drive_on(self, distance, self.conditioner_add_fuel)

    def refuel(self, fuel) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    conditioner_add_fuel = 1.6
    fuel_reduction = 0.95

    def drive(self, distance) -> None:
        Vehicle.drive_on(self, distance, self.conditioner_add_fuel)

    def refuel(self, fuel) -> None:
        self.fuel_quantity += fuel * self.fuel_reduction


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
