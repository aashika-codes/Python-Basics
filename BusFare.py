class vehicle:
    def __init__(self,fare):
        self.fare=fare
class bus(vehicle):
    pass
bus_fare=bus(24.50)
print("The total fare of your bus ride is", bus_fare.fare)