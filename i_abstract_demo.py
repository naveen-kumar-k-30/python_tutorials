from abc import ABC, abstractmethod

''' you cannot create obj for abs class 
and all inherit class must define all the abs functions 
and abs is said to be blueprint of other sub classes

'''


class Vehicle(ABC):  # abstract class
    @abstractmethod  # decorator
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):  # concrete class
    color = None

    def start(self):
        print("car started")

    def stop(self):
        print("car stopped")

class Bike(Vehicle):  # concrete class
    color = None

    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")
