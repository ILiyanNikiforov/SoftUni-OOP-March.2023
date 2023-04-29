from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Dog:
    name: str
    age: int
    foods: List = field(default_factory=list)
    muzzle: Optional[bool] = False

    def __str__(self):
        return f"Name: {self.name}; Age: {self.age} with favorite food: {', '.join(self.foods)}"

    def add_food(self, food):
        if food not in self.foods:
            self.foods.append(food)


my_dog = Dog("Sharo", 7)
my_dog2 = Dog("Blacky", 11)
my_dog.add_food("meat")
my_dog.add_food("bones")
my_dog.add_food("cheese")
my_dog2.add_food("bones")

print(my_dog)
# print(my_dog.foods)
# print(my_dog2)
# print(my_dog2.foods)

print(my_dog.__dict__)
