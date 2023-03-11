from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def find_customer(self, customer_id: int):
        for customer in self.customers:
            if customer.id == customer_id:
                current_customer = customer
                return current_customer

    def find_dvd(self, dvd_id: int):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                current_dvd = dvd
                return current_dvd

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer = MovieWorld.find_customer(self, customer_id)
        current_dvd = MovieWorld.find_dvd(self, dvd_id)

        if current_dvd and current_customer:
            if current_dvd in current_customer.rented_dvds:
                return f"{current_customer.name} has already rented {current_dvd.name}"
            elif current_dvd.is_rented:
                return "DVD is already rented"
            elif current_customer.age < current_dvd.age_restriction:
                return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

            current_customer.rented_dvds.append(current_dvd)
            current_dvd.is_rented = True
            return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        current_customer = MovieWorld.find_customer(self, customer_id)
        current_dvd = MovieWorld.find_dvd(self, dvd_id)

        if current_dvd and current_customer:
            if current_dvd in current_customer.rented_dvds:
                current_customer.rented_dvds.remove(current_dvd)
                current_dvd.is_rented = False
                return f"{current_customer.name} has successfully returned {current_dvd.name}"
            return f"{current_customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += f'{customer}\n'
        for dvd in self.dvds:
            result += f'{dvd}\n'
        return result


