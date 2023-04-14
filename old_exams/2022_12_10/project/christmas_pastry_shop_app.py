from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class DelicacyFactory:
    @staticmethod
    def produce_musician(type_delicacy, name, price):
        if type_delicacy == "Gingerbread":
            return Gingerbread(name, price)
        elif type_delicacy == "Stolen":
            return Stolen(name, price)


class BoothFactory:
    @staticmethod
    def produce_musician(type_booth, booth_number, capacity):
        if type_booth == "Open Booth":
            return OpenBooth(booth_number, capacity)
        elif type_booth == "Private Booth":
            return PrivateBooth(booth_number, capacity)


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: List[Booth] = []           # list that will contain all booths (objects) that are created
        self.delicacies: List[Delicacy] = []    # list that will contain all delicacies (objects) that are created
        self.income = 0.0                       # total income of the pastry shop.

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if [d for d in self.delicacies if d.name == name]:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in ["Gingerbread", "Stolen"]:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = DelicacyFactory.produce_musician(type_delicacy, name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if [b for b in self.booths if b.booth_number == booth_number]:
            raise ValueError(f"Booth number {booth_number} already exists!")

        if type_booth not in ["Open Booth", "Private Booth"]:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = BoothFactory.produce_musician(type_booth, booth_number,capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        if not [b for b in self.booths if b.capacity >= number_of_people and not b.is_reserved]:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth = [b for b in self.booths if b.capacity >= number_of_people and not b.is_reserved][0]

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        if not [b for b in self.booths if b.booth_number == booth_number]:
            raise Exception(f"Could not find booth {booth_number}!")

        if not [d for d in self.delicacies if d.name == delicacy_name]:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        delicacy = [d for d in self.delicacies if d.name == delicacy_name][0]

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        current_bill = booth.take_bill()
        booth.delicacy_orders.clear()
        booth.price_for_reservation = 0
        booth.is_reserved = False
        self.income += current_bill

        return f"Booth {booth.booth_number}:\n" \
               f"Bill: {current_bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."




