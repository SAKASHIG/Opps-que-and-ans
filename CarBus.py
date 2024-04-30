class Vehicle:
    def _init_(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")

    def stop_engine(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")


class Bus(Vehicle):
    def _init_(self, make, model, capacity):
        super()._init_(make, model)
        self.capacity = capacity

    def Start_bus(self):
        print(f"Capacity: {self.capacity}")


b = Bus(make="Custom Bus", model="2001", capacity=50)
b.start_engine()
b.start_bus()
b.stop_engine()

Vehicle.color = "white"
v = Vehicle(make="BMW", model="2005")
print(f"My vehicle color: {Vehicle.color}")