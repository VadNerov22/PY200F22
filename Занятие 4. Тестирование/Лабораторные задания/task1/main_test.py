import unittest
from main import Cars


class MyTestCase(unittest.TestCase):

    def test_car_capacity_volume_f(self):
        self.assertRaises(TypeError, Cars.car_capacity_volume_f, "212")

    def test_car_occupied_volume_f(self):
        self.assertRaises(TypeError, Cars.car_occupied_volume_f, "158")

    def test_is_valid_car_type(self):
        self.assertTrue(Cars.is_valid_car_type("седан"))
        self.assertRaises(TypeError, Cars.is_valid_car_type, 15)
        self.assertRaises(ValueError, Cars.is_valid_car_type, "джип")

    def test_mile_h_to_km_h(self):
        self.assertEqual(Cars.mile_h_to_km_h(90), 144)

    def test_to_kbt(self):
        self.assertEqual(Cars.to_kbt(150), 110)

    def setUp(self):
        self._car_capacity_volume_f = 58
        self._car_occupied_volume_f = 20

    def test_power_reserve(self):
        self.assertEqual(Cars.power_reserve(self, 380), 200)

    def test_is_valid_init(self):
        self.assertRaises(TypeError, Cars.is_valid_init, 120.15)
        self.assertRaises(ValueError, Cars.is_valid_init, -15)


if __name__ == '__main__':
    unittest.main()
