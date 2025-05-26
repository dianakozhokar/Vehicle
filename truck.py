from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, make, model, year, weight, cargo_capacity, towing_capacity):
        super().__init__(make, model, year, weight)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity

    def start_engine(self):  # Обов'язково цей метод!
        print("The truck's engine is starting...")

    def haul(self):
        print(f"{self.model} is hauling {self.cargo_capacity} kg.")
