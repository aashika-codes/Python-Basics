class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus(Vehicle):
    pass 
school_bus=Bus("School Bus Volvo", 112,21)
print("Vehicle name is:", school_bus.name, "speed is:",school_bus.max_speed, "Mileage is:", school_bus.mileage)