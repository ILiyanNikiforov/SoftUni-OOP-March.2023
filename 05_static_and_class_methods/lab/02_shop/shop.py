class Shop:

    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = dict()

    @classmethod
    def small_shop(cls, name: str, type_shop: str):
        SMALL_SHOP_CAPACITY = 10
        return cls(name, type_shop, SMALL_SHOP_CAPACITY)

    def add_item(self, item_name: str):
        if sum(self.items.values()) == self.capacity:
            return "Not enough capacity in the shop"
        elif item_name not in self.items:
            self.items[item_name] = 0

        self.items[item_name] += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int):
        if item_name not in self.items or self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount
        if self.items[item_name] == 0:
            del self.items[item_name]

        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Bananas", 1))
print(fresh_shop.remove_item("Tomatoes", 2))
print(fresh_shop.items)
