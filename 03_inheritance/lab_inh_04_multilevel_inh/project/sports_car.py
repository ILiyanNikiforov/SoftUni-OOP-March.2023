from project.car import Car


class SportsCar(Car):
    def race(self):
        return "racing..."


my_car = SportsCar()
print(my_car.race())
print(my_car.drive())
print(my_car.move())
