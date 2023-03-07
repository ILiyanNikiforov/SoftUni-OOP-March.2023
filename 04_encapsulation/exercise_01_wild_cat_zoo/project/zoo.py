from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) < self.__animal_capacity:
            if self.__budget >= price:
                self.__budget -= price
                self.animals.append(animal)
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            elif self.__budget < price:
                return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.__workers_capacity -= 1
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([worker.salary for worker in self.workers])

        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_for_care = sum([animal.money_for_care for animal in self.animals])

        if total_money_for_care <= self.__budget:
            self.__budget -= total_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f'You have {len(self.animals)} animals']
        animals_dict = {"Lion": [], "Tiger": [], "Cheetah": []}
        for animal in self.animals:
            if str(animal.__class__.__name__) in animals_dict.keys():
                animals_dict[animal.__class__.__name__].append(animal)

        for type_animal, animals in animals_dict.items():
            result.append(f"----- {len(animals_dict[type_animal])} {type_animal}s:")
            for animal in animals:
                result.append(animal.__repr__())
        return "\n".join(result)

    def workers_status(self):
        result = [f'You have {len(self.workers)} workers']
        workers_dict = {"Keeper": [], "Caretaker": [], "Vet": []}

        for worker in self.workers:
            if str(worker.__class__.__name__) in workers_dict.keys():
                workers_dict[worker.__class__.__name__].append(worker)

        for type_worker, workers in workers_dict.items():
            result.append(f"----- {len(workers_dict[type_worker])} {type_worker}s:")
            for worker in workers:
                result.append(worker.__repr__())

        return "\n".join(result)





