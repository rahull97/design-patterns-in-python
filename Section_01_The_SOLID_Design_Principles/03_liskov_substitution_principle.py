# Liskov substitution principle states that " Objects in a program should be replace-able
# with the instances of their subtypes without altering the correctness of that program


# Breaking - Liskov substitution principle example
class Car:
    def __init__(self, car_type):
        self.type = car_type


class PetrolCar(Car):
    def __init__(self, car_type):
        super().__init__(car_type)


car = Car("SUV")
car.properties = {"Color": "Red", "Capacity": 6}

petrol_car = PetrolCar("BMW")
petrol_car.properties = ("Red", 5)

# find the cars with red color
cars = [car, petrol_car]

# the below code will throw error as we do not follow LSP, because in super class "car"
# properties are set using dictionary and in child class "petrol car" properties are set
# using tuple. Thus, we cannot replace objects of super type with child type w/o altering
# program behaviour

red_cars = 0
for car in cars:
    if car.properties["Color"] == "Red":
        red_cars = red_cars + 1


# Correct Implementation - Liskov substitution principle example
class Car:
    def __init__(self, car_type):
        self.type = car_type
        self.car_props = {}

    def set_properties(self, color, capacity):
        self.car_props = {"Color": color, "Capacity": capacity}

    def get_properties(self):
        return self.car_props


class PetrolCar(Car):
    def __init__(self, car_type):
        super().__init__(car_type)


car = Car("SUV")
car.set_properties("Blue", 6)

petrol_car = PetrolCar("BMW")
petrol_car.set_properties("Blue", 6)

# find the cars with blue color
cars = [car, petrol_car]

# follow LSP, as objects of super class can be replaced with objects of child class
# and behaviour of the program is not altered.
blue_cars = 0
for car in cars:
    if car.properties["Color"] == "Red":
        red_cars = blue_cars + 1
