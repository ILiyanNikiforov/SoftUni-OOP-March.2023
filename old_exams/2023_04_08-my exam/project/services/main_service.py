from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=MainService.CAPACITY)

    def details(self):
        robots = " ".join(r.name for r in self.robots)
        return f"{self.name} Main Service:\nRobots: {robots if robots else 'none'}"

# x = MainService("Pesho")
# x.robots = []
#
# print(x.details())
