from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors, num_passengers):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors
        self.num_passengers = num_passengers

    def start_engine(self):
        print("The car's engine is starting...")

    def drive(self):
        print(f"{self.model} is driving with {self.num_passengers} passengers.")
