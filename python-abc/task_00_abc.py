#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""importing ABC and abstractmethod from abc module"""


class Animal(ABC):
    """Create an Animal class"""
    @abstractmethod
    def sound(self):
        """Create an sound abstract method"""
        pass

class Dog(Animal):
    """ Create a Dog Class"""
    def sound(self):
        """Create a sound method for Dog"""
        return "Bark"
    
class Cat(Animal):
    """Create a Cqat Class"""
    def sound(self):
        """Create a sound method for Cat"""
        return "Meow"
