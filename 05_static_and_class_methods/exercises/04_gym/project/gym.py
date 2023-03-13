from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List = []
        self.trainers: List = []
        self.equipment: List = []
        self.plans: List = []
        self.subscriptions: List = []

    def add_customer(self, customer: Customer):
        self.__add_entity(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.__add_entity(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.__add_entity(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_entity(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.__find_entity_by_id(self.subscriptions, subscription_id)
        customer = self.__find_entity_by_id(self.customers, subscription.customer_id)
        trainer = self.__find_entity_by_id(self.trainers, subscription.trainer_id)
        exercise = self.__find_entity_by_id(self.plans, subscription.exercise_id)
        equipment = self.__find_entity_by_id(self.equipment,exercise.equipment_id)

        result = [repr(subscription), repr(customer), repr(trainer), repr(equipment), repr(exercise)]
        return "\n".join(str(x) for x in result)

    def __find_entity_by_id(self, collection, entity_id: int):
        for entity in collection:
            if entity.id == entity_id:
                return entity



    @staticmethod
    def __add_entity(entity, collection):
        if entity in collection:
            return
        collection.append(entity)


