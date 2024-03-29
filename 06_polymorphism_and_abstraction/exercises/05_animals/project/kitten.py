from project.cat import Cat


class Kitten(Cat):
    GENDER = "Female"

    def __init__(self, name, age):
        super().__init__(name, age, gender=self.GENDER)

    def make_sound(self):
        return "Meow"
