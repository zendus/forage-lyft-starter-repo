from .tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear_array: list):
        self.tire_wear_array = tire_wear_array

    def needs_service(self) -> bool:
        return len([i for i in self.tire_wear_array if i >= 0.9]) >= 1