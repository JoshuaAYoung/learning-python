# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

# classes allow you to group lots of data together (sort of like a component in JS?)

class Vehicle:
  def __init__(self, bodystyle):
    self.bodystyle = bodystyle

  def drive(self, speed):
    self.mode = "driving"
    self.speed = speed

# car automatically gets access to vehicle parameter
class Car(Vehicle):
  def __init__(self, enginetype):
    super().__init__("Car")
    self.wheels = 4
    self.doors = 4
    self.engine = enginetype

# overriding the drive function from Vehicle here
  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.engine, "car at", self.speed)

class Motorcycle(Vehicle):
  def __init__(self, enginetype, hassidecar):
    super().__init__("Motorcycle")
    if (hassidecar):
      self.wheels = 3
    else:
      self.wheels = 2
    
    self.doors = 0
    self.enginetype = enginetype

  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.enginetype, "motorcycle at", self.speed)

car1 = Car("gas")
car2 = Car("electric")
motorcycle1 = Motorcycle("gas", True)

print(motorcycle1.wheels)
print(car1.doors)
print(car2.engine)

car1.drive(50)
motorcycle1.drive(30)