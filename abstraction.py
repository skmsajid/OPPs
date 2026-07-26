#Means hiding the complex internal implementation details 
# and showing only the essential features to the user. 
# It acts as a blueprint for other classes.

# In Python
# Python does not support abstraction by default. 
# We achieve it by importing the ABC (Abstract Base Class) class and 
# the @abstractmethod decorator from the built-in abc module.
from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")


c = Car()

c.start()