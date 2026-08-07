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


"""
R-2.5
Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter.
"""

#solution
"""the following is a revised version of the charge and make_payment methods
of the CreditCard class that ensures the caller sends a number as a parameter:
"""

class CreditCard:
    def __init__(self, customer, bank, account, limit):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = 0

    def charge(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        if amount + self.balance > self.limit:
            return False
        else:
            self.balance += amount
            return True

    def make_payment(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        self.balance -= amount


"""
R-2.6
If the parameter to the make payment method of the CreditCard class
were a negative number, that would have the effect of raising the balance
on the account. Revise the implementation so that it raises a ValueError if
a negative value is sent.
"""
#solution


def make_payment(self, amount):
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number.")
    if amount < 0:
        raise ValueError("Payment amount cannot be negative.")
    self.balance -= amount


"""
R-2.7
The CreditCard class of Section 2.3 initializes the balance of a new ac-
count to zero. Modify that class so that a new account can be given a
nonzero balance using an optional fifth parameter to the constructor. The
four-parameter constructor syntax should continue to produce an account
with zero balance.
"""

#solution
class CreditCard:
    def __init__(self, customer, bank, account, limit, balance=0):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = balance






