import unittest

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestTires(unittest.TestCase):

    def test_carrigan_tire_should_be_serviced(self):
        tire_wear_array = [0, 0, 0.9, 0]
        carrigan_tire = CarriganTire(tire_wear_array)
        
        self.assertTrue(carrigan_tire.needs_service())

    def test_carrigan_tire_should_not_be_serviced(self):
        tire_wear_array = [0, 0.2, 0, 0]
        carrigan_tire = CarriganTire(tire_wear_array)
        
        self.assertFalse(carrigan_tire.needs_service())

    def test_octoprime_tire_should_be_serviced(self):
        tire_wear_array = [1, 0.5, 1, 0.9]
        octoprime_tire = OctoprimeTire(tire_wear_array)

        self.assertTrue(octoprime_tire.needs_service())

    def test_octoprime_tire_should_not_be_serviced(self):
        tire_wear_array = [0, 1, 1, 0.9]
        octoprime_tire = OctoprimeTire(tire_wear_array)

        self.assertFalse(octoprime_tire.needs_service())