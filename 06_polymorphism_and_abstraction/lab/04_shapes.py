import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius

    def calculate_area(self):
        return math.pi * self.__radius * self.__radius


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.__height = height
        self.__width = width

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)

    def calculate_area(self):
        return self.__width * self.__height








