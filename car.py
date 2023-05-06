# Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
class Car:
    wheels = 4
    def __init__(self,color,make,model):
          self.color = color
          self.make = make
          self.model = model
    def car_capacity(self):
        return f"my {self.color} {self.make} has three sits"
    def start_car(self):
        return f"my {self.make} starts by making a funny noise"
    def car_speed(self):
        return f"my {self.make} {self.model} moves at a very high speed"
    