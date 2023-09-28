import unittest
from datetime import datetime

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class TestBattery(unittest.TestCase):
    
    def test_nubbin_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        nubbin_battery = NubbinBattery(last_service_date, today)
        self.assertTrue(nubbin_battery.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        nubbin_battery = NubbinBattery(last_service_date, today)
        self.assertFalse(nubbin_battery.needs_service())

    def test_spindler_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        spindler_battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(spindler_battery.needs_service())

    def test_spindler_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        spindler_battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(spindler_battery.needs_service())



if __name__ == '__main__':
    unittest.main()