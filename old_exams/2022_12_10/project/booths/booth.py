from abc import ABC, abstractmethod
from typing import List


class Booth(ABC):
    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number         # The value represents the booth's number.
        self.capacity = capacity                 # The value represents the booth's capacity.
        self.delicacy_orders: List = []          # List with delicacies (objects) that are ordered.
        self.price_for_reservation: float = 0    # When booth is reserved, the price for a reservation should be set.
        self.is_reserved = False                 # Set to True if the booth is reserved, otherwise False.

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity cannot be a negative number!")
        self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people: int):
        pass

    def take_bill(self):
        return self.price_for_reservation + sum(d.price for d in self.delicacy_orders)
