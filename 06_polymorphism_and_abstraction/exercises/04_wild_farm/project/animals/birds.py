from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    FOOD_TYPE_EATEN = [Meat]
    WEIGHT_INCREASE = 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def type_food_eat(self):
        return self.FOOD_TYPE_EATEN

    @property
    def weight_increase(self):
        return self.WEIGHT_INCREASE


class Hen(Bird):
    FOOD_TYPE_EATEN = [Vegetable, Fruit, Meat, Seed]
    WEIGHT_INCREASE = 0.35

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def type_food_eat(self):
        return self.FOOD_TYPE_EATEN

    @property
    def weight_increase(self):
        return self.WEIGHT_INCREASE
