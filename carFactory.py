from datetime import date
from abc import ABC, abstractmethod
from car import Car
from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, sternman_engine, willoughby_engine



class CarFactory:

    @staticmethod
    def create_calliope(current_mileage, last_service_mileage, last_service_date, current_date) -> Car:
        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        return Car(engine=engine, battery=battery)

    @staticmethod
    def create_glissade(current_mileage, last_service_mileage, last_service_date, current_date) -> Car:
        engine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        return Car(engine=engine, battery=battery)
    
    @staticmethod
    def create_palindrome(warning_light_on, last_service_date, current_date) -> Car:
        engine = sternman_engine.SternmanEngine(warning_light_on)
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        return Car(engine=engine, battery=battery)
    
    @staticmethod
    def create_rorschach(current_mileage, last_service_mileage, last_service_date, current_date) -> Car:
        engine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        return Car(engine=engine, battery=battery)
    
    @staticmethod
    def create_thovex(current_mileage, last_service_mileage, last_service_date, current_date) -> Car:
        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        return Car(engine=engine, battery=battery)






