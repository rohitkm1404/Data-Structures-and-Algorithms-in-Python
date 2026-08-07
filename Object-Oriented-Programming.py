#exercise solutions for object-oriented programming
"""--------------------------------------------------Reinforcement-------------------------------------------------"""

"""
R-2.1 
Give three examples of life-critical software applications.
"""

#solution

"""
1. Air Traffic Control Systems:
 These systems manage the safe and efficient movement of aircraft in the airspace and on the ground.
Any failure in this software could lead to catastrophic accidents.

2. Car Airbag Control Systems:
 These systems are responsible for deploying airbags in the event of a collision.
A malfunction could result in airbags not deploying during an accident, leading to severe injuries or fatalities.

3.Truck Anti-lock Braking Systems (ABS):
 These systems prevent the wheels from locking up during braking, allowing the driver to maintain steering control.

"""


"""
R-2.2
Give an example of a software application in which adaptability can mean
the difference between a prolonged lifetime of sales and bankruptcy.
"""
#solution

"""
An example of a software application where adaptability 
is crucial is a mobile operating system, such as Android or iOS.
"""


"""
R-2.3
Describe a component from a text-editor GUI and the methods that it encapsulates.
"""

#solution

"""
A component from a text-editor GUI could be the "Text Area"where users input 
and edit their text.
Methods that it might encapsulate include:
- insert_text(): Insert text at a specific position.
- delete_text(): Delete text within a specified range.
- get_text(): Retrieve the current text content.
- set_text(): Set the text content.
"""

"""
R-2.4
Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its num-
ber of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
"""

#solution

class Flower:
    def __init__(self, name: str, num_petals: int, price: float):
        self.name = name
        self.num_petals = num_petals
        self.price = price

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_num_petals(self, num_petals: int):
        self.num_petals = num_petals

    def get_num_petals(self) -> int:
        return self.num_petals

    def set_price(self, price: float):
        self.price = price

    def get_price(self) -> float:
        return self.price

