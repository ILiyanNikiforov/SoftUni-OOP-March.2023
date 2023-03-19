from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return ('woof-woof')


class Cat(Animal):
    def make_sound(self):
        return ('meow')


class Chicken(Animal):
    def make_sound(self):
        return('pew-pew')


animals = [Cat(), Dog(), Chicken()]


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animal_sound(animals)


