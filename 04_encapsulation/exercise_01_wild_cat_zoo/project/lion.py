from project.animal import Animal


class Lion(Animal):
    DEFAULT_MONEY_FOR_CARE = 50

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Lion.DEFAULT_MONEY_FOR_CARE)
