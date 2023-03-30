from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.m = Mammal("Buddy", "Dog", "Wof-wof")

    def test_correct_name(self):
        m = Mammal("Buddy", "Dog", "Wof-wof")
        self.assertEqual("Buddy", m.name)

    def test_correct_type(self):
        m = Mammal("Buddy", "Dog", "Wof-wof")
        self.assertEqual("Dog", m.type)

    def test_correct_sound(self):
        m = Mammal("Buddy", "Dog", "Wof-wof")
        self.assertEqual("Wof-wof", m.sound)

    def test_correct_type_mammal(self):
        m = Mammal("Buddy", "Dog", "Wof-wof")
        self.assertEqual("animals", m._Mammal__kingdom)

    def test_correct_info(self):
        expected = f"{self.m.name} is of type {self.m.type}"
        result = self.m.info()
        self.assertEqual(expected, result)

    def test_correct_make_sound(self):
        expected = f"{self.m.name} makes {self.m.sound}"
        result = self.m.make_sound()
        self.assertEqual(expected, result)

    def test_correct_kingdom(self):
        self.assertEqual(self.m.get_kingdom(), self.m._Mammal__kingdom)


if __name__ == "__main__":
    main()
