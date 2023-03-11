from typing import List


class Customer:
    def __init__(self, name: str, age: int, id_num: int):
        self.name = name
        self.age = age
        self.id = id_num
        self.rented_dvds: List = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)}" \
               f" rented DVD's ({', '.join([movie.name for movie in self.rented_dvds])})"
