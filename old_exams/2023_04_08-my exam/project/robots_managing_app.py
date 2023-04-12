from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class ServiceFactory:
    @staticmethod
    def create_service(service_type, name):
        if service_type == "MainService":
            return MainService(name)
        elif service_type == "SecondaryService":
            return SecondaryService(name)


class RobotFactory:
    @staticmethod
    def create_robot(robot_type, name, kind, price):
        if robot_type == "MaleRobot":
            return MaleRobot(name, kind, price)
        elif robot_type == "FemaleRobot":
            return FemaleRobot(name, kind, price)


class RobotsManagingApp:
    VALID_SERVICES = ["MainService", "SecondaryService"]
    VALID_ROBOT_TYPES = ["MaleRobot", "FemaleRobot"]

    def __init__(self):
        self.robots: list = []          # list that will contain all robots (objects)
        self.services: list = []        # list that will contain all services(objects)

    def add_service(self, service_type: str, name: str):
        if service_type not in RobotsManagingApp.VALID_SERVICES:
            raise Exception("Invalid service type!")

        service = ServiceFactory.create_service(service_type, name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in RobotsManagingApp.VALID_ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        robot = RobotFactory.create_robot(robot_type, name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]
        if (isinstance(robot, FemaleRobot) and isinstance(service, MainService))\
                or (isinstance(robot, MaleRobot) and isinstance(service, SecondaryService)):
            return "Unsuitable service."

        if service.capacity > len(service.robots):
            service.robots.append(robot)
            self.robots.remove(robot)
            return f"Successfully added {robot_name} to {service_name}."
        raise Exception("Not enough capacity for this robot!")

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.__find_service_by_name(service_name)
        if not [r for r in service.robots if r.name == robot_name]:
            raise Exception("No such robot in this service!")

        robot = [r for r in service.robots if r.name == robot_name][0]
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.__find_service_by_name(service_name)
        for robot in service.robots:
            robot.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        final_price = 0

        for robot in service.robots:
            final_price += robot.price
        return f"The value of service {service_name} is {final_price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())

        result_to_print = '\n'.join(result)
        return f"{result_to_print}"

    def __find_service_by_name(self, service_name):
        if [s for s in self.services if s.name == service_name]:
            return [s for s in self.services if s.name == service_name][0]

    def __find_robot_by_name(self, robot_name):
        if [r for r in self.robots if r.name == robot_name]:
            return [r for r in self.robots if r.name == robot_name][0]
