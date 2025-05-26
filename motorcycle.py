from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, weight, num_wheels, has_sidecar):
        super().__init__(make, model, year, weight)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar

    def start_engine(self):
        print("The motorcycle's engine is starting...")

    def ride(self):
        if self.has_sidecar:
            print(f"{self.model} is riding with a sidecar.")
        else:
            print(f"{self.model} is riding without a sidecar.")
