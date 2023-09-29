from .tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear_array: list):
        self.tire_wear_array = tire_wear_array

    def needs_service(self) -> bool:
        return sum(self.tire_wear_array) >= 3