from datetime import date
from abc import ABC, abstractmethod
from car import Car
from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, sternman_engine, willoughby_engine



class CarFactory():

    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, warning_light_on: bool):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_on = warning_light_on

    def create_calliope(self) -> Car:
        engine = capulet_engine.CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = spindler_battery.SpindlerBattery(self.last_service_date, self.current_date)
        return Car(engine=engine, battery=battery)

    def create_glissade(self) -> Car:
        engine = willoughby_engine.WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        battery = spindler_battery.SpindlerBattery(self.last_service_date, self.current_date)
        return Car(engine=engine, battery=battery)
    
    def create_palindrome(self) -> Car:
        engine = sternman_engine.SternmanEngine(self.warning_light_on)
        battery = spindler_battery.SpindlerBattery(self.last_service_date, self.current_date)
        return Car(engine=engine, battery=battery)
    
    def create_rorschach(self) -> Car:
        engine = willoughby_engine.WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        battery = nubbin_battery.NubbinBattery(self.last_service_date, self.current_date)
        return Car(engine=engine, battery=battery)
    
    def create_thovex(self) -> Car:
        engine = capulet_engine.CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = nubbin_battery.NubbinBattery(self.last_service_date, self.current_date)
        return Car(engine=engine, battery=battery)






