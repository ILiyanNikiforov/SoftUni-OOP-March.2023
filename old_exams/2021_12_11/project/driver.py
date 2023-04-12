
class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car = None             # One driver drives ONLY one car. type Car
        self.number_of_wins = 0     # When the driver wins a race, the number of wins should be increased!

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name should contain at least one character!")
        self.__name = value
