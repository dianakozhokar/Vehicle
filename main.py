from car import Car
from truck import Truck
from motorcycle import Motorcycle

car = Car("Toyota", "Corolla", 2020, 1300, 4, 5)
truck = Truck("Volvo", "FH", 2018, 8000, 20000, 30000)
motorcycle = Motorcycle("Harley-Davidson", "Iron 883", 2022, 250, 2, False)

car.drive()
truck.haul()
motorcycle.ride()

print("\nStarting engines:")
for vehicle in [car, truck, motorcycle]:
    vehicle.start_engine()
