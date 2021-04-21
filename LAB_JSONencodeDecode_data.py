"""
Your task is to write a code which has exactly the same conversation with the user and:

defines a class named Vehicle, whose objects can carry the vehicle data shown
above (the structure of the class should be deducted from the above dialog
— call it "reverse engineering" if you want)
defines a class able to encode the Vehicle object into an
equivalent JSON string;
defines a class able to decode the JSON string into the
newly created Vehicle object.

"""

import json

class Vehicle:
    def __init__(self, registration_number, model, passenger, mass):
        self.registration_number = registration_number
        self.model = model
        self.passengers = False if passenger=='n' else True
        self.mass = mass

class MyEncoder(json.JSONEncoder):
    def default(self, v_obj):
        if isinstance(v_obj, Vehicle):
            return v_obj.__dict__
        else:
            return super().default(self, z)

class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_vehicle)

    def decode_vehicle(self, d):
        return Vehicle(**d)

def choice1():
    reg = input("Registration number: ")
    year = int(input("Year of production: "))
    passenger = input("Passengers [y/n]: ")
    mass = int(input("Vehicle mass: "))
    new_vehicle = Vehicle(reg, year, passenger, mass)
    print(json.dumps(new_vehicle, cls=MyEncoder))

def choice2():
    json_string = '{"registration_number":"PC38927Z", "model":2018, "passenger": false, "mass":1543.2}'
    new_vehicle = json.loads(json_string, cls=MyDecoder)
    print(new_vehicle.__dict__)

choice = None
while choice not in [1,2]:
    try:
        choice = int(input("What can i do for you?\
         \n 1 - Produce a JSON string describing a vehicle\
          \n 2 - decode a JSON string into a vehicle\
          \nyour choice: "))
    except Exception as e:
        print("please enter a number 1 or 2")

if choice == 1:
    choice1()
if choice == 2:
    choice2()
