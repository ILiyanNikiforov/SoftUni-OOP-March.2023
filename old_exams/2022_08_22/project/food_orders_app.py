from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []  # list that contains all the meals (objects)
        self.clients_list: list[Client] = []  # list that contains all the clients (objects)

    @staticmethod
    def get_next_id():
        result = FoodOrdersApp.receipt_id
        FoodOrdersApp.receipt_id += 1
        return result

    def __find_client(self, client_phone_number):
        if [c for c in self.clients_list if c.phone_number == client_phone_number]:
            return [c for c in self.clients_list if c.phone_number == client_phone_number][0]

    def __find_meal(self, meal_name):
        if [m for m in self.menu if m.name == meal_name]:
            return [m for m in self.menu if m.name == meal_name][0]

    def register_client(self, client_phone_number: str):
        if self.__find_client(client_phone_number):
            raise Exception("The client has already been registered!")
        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        meals = [meal.details() for meal in self.menu]
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        return "\n".join(meals)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantity):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        if not self.__find_client(client_phone_number):
            self.register_client(client_phone_number)
        client = self.__find_client(client_phone_number)
        meals_to_order = []
        current_bill = 0

        for meal_name, meal_quantity in meal_names_and_quantity.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_quantity:
                        meals_to_order.append(meal)
                        current_bill += meal.price * meal_quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        for meal_name, meal_quantity in meal_names_and_quantity.items():
            if meal_name not in client.current_shopping:
                client.current_shopping[meal_name] = 0
            client.current_shopping[meal_name] += meal_quantity
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_quantity

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__find_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        for ordered_meal, quantity in client.current_shopping.items():
            for menu_meal in self.menu:
                if ordered_meal == menu_meal.name:
                    menu_meal.quantity += quantity
        client.shopping_cart = []
        client.bill = 0
        client.current_shopping = {}
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        client.bill = 0
        client.shopping_cart = []
        client.current_shopping = {}
        receipt_id = self.get_next_id()
        return f"Receipt #{receipt_id} with total amount of {total_paid_money:.2f}" \
               f" was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

