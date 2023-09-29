from datetime import date
from abc import ABC, abstractmethod
from car import Car
from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, sternman_engine, willoughby_engine
from tire import carrigan_tire, octoprime_tire



class CarFactory:

    @staticmethod
    def create_calliope(current_mileage, last_service_mileage, last_service_date, current_date, tire_wear_array) -> Car:
        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        tire = carrigan_tire.CarriganTire(tire_wear_array)
        return Car(engine=engine, battery=battery, tire=tire)

    @staticmethod
    def create_glissade(current_mileage, last_service_mileage, last_service_date, current_date, tire_wear_array) -> Car:
        engine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        tire = octoprime_tire.OctoprimeTire(tire_wear_array)
        return Car(engine=engine, battery=battery, tire=tire)
    
    @staticmethod
    def create_palindrome(warning_light_on, last_service_date, current_date, tire_wear_array) -> Car:
        engine = sternman_engine.SternmanEngine(warning_light_on)
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        tire = carrigan_tire.CarriganTire(tire_wear_array)
        return Car(engine=engine, battery=battery, tire=tire)
    
    @staticmethod
    def create_rorschach(current_mileage, last_service_mileage, last_service_date, current_date, tire_wear_array) -> Car:
        engine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        tire = octoprime_tire.OctoprimeTire(tire_wear_array)
        return Car(engine=engine, battery=battery, tire=tire)
    
    @staticmethod
    def create_thovex(current_mileage, last_service_mileage, last_service_date, current_date, tire_wear_array) -> Car:
        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        tire = carrigan_tire.CarriganTire(tire_wear_array)
        return Car(engine=engine, battery=battery, tire=tire)






