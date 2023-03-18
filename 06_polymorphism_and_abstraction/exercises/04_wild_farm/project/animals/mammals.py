from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    FOOD_TYPE_EATEN = [Vegetable, Fruit]
    WEIGHT_INCREASE = 0.10

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def type_food_eat(self):
        return self.FOOD_TYPE_EATEN

    @property
    def weight_increase(self):
        return self.WEIGHT_INCREASE


class Dog(Mammal):
    FOOD_TYPE_EATEN = [Meat]
    WEIGHT_INCREASE = 0.40

    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def type_food_eat(self):
        return self.FOOD_TYPE_EATEN

    @property
    def weight_increase(self):
        return self.WEIGHT_INCREASE


class Cat(Mammal):
    FOOD_TYPE_EATEN = [Vegetable, Meat]
    WEIGHT_INCREASE = 0.30

    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def type_food_eat(self):
        return self.FOOD_TYPE_EATEN

    @property
    def weight_increase(self):
        return self.WEIGHT_INCREASE


class Tiger(Mammal):
    FOOD_TYPE_EATEN = [Meat]
    WEIGHT_INCREASE = 1

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def type_food_eat(self):
        return self.FOOD_TYPE_EATEN

    @property
    def weight_increase(self):
        return self.WEIGHT_INCREASE
