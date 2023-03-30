from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(100, 250)

    def test_vehicle_init(self):
        fuel = 100
        hp = 250
        vehicle = Vehicle(fuel, hp)

        self.assertEquals(fuel, vehicle.fuel)
        self.assertEquals(fuel, vehicle.capacity)
        self.assertEquals(hp, vehicle.horse_power)
        self.assertEquals(Vehicle.fuel_consumption, vehicle.fuel_consumption)

    def test_str_returns_proper_text(self):
        expected = f"The vehicle has {self.car.horse_power} " \
               f"horse power with {self.car.fuel} fuel left and {self.car.fuel_consumption} fuel consumption"
        result = str(self.car)

        self.assertEqual(expected, result)

    def test_raise_if_not_enough_fuel_for_drive_distance(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(90)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_decrease_fuel_when_distance_is_reachable(self):
        distance = 10
        current_fuel = self.car.fuel
        needed_fuel = distance * 1.25
        expected = current_fuel - needed_fuel

        self.assertEqual(100, self.car.fuel)
        self.car.drive(distance)
        self.assertEqual(expected, self.car.fuel)

    def test_drive_equal_fuel_if_decrease_fuel(self):
        self.assertEqual(100, self.car.fuel)
        self.car.drive(100/1.25)
        self.assertEqual(0, self.car.fuel)

    def test_refuel_if_fuel_is_more_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_if_there_is_capacity(self):
        self.car.fuel = 50
        self.car.refuel(50)
        self.assertEqual(100, self.car.fuel)



