import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestEngine(unittest.TestCase):
    
    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 70_000
        last_service_mileage = 20_000

        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet_engine.needs_service())

    def test_capulet_engine_should_not_be_serviced(self):
        current_mileage = 5_000
        last_service_mileage = 30_000

        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet_engine.needs_service())

    def test_sternman_engine_should_be_serviced(self):
        warning_light_is_on = True

        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman_engine.needs_service())

    def test_sternman_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman_engine.needs_service())

    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 90_000
        last_service_mileage = 10_000

        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby_engine.needs_service())

    def test_willoughby_engine_should_not_be_serviced(self):
        current_mileage = 70_000
        last_service_mileage = 20_000

        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby_engine.needs_service())



if __name__ == '__main__':
    unittest.main()